
# coding: utf-8

# # Cognitive Services "coffee choice" Personalizer demo 
# https://github.com/Azure-Samples/cognitive-services-personalizer-samples

# In this example, we will use Azure Personalizer Service to predict what Coffee a person (Alice, Bob, Cathy and Dave) prefers using the weather condition and time of day. File "example.json" contains their preferred choices of coffee (set deterministically for the simplicity of this example). We will compare this data with the predictions from the service and generate rewards (0 or 1) based on the match and send it back to the service for training the model, to learn each person's preferences.
# 
# Note that a model is exported every 5 minutes (current default) if you are using the Cognitive Services instance of the Personalizer service, so you need to wait at least until that time has expired then to actually observe some learning in the rewards returned. Exploration is set at 20%. You can experiment with the model training defaults in the Settings blade for the Personalizer resource in the [Azure Portal](https://ms.portal.azure.com).
# 
# This implementation calls the [Personalizer service RESTful API](https://westus2.dev.cognitive.microsoft.com/docs/services/personalizer-api/operations/Rank); a set of http requests that the Personalizer exposes. The model iterates over events, performing _on-line learning._ The sequence of operation is
# 
# - Observe the features (simulated in this demo) of the current event: The weather and time of day for this person's coffee choice.
# - Place a _rank request_ to the Personalizer Service, using the model to predict the person's preferred choice from the set of specified _actions_.
# - Compare the person's true choice with the predicted, and compute a model _reward_: 1 if they agree, 0 otherwise.
# - Send the _reward_ back to the Service, to train the model on persons' preferences.
# 
# We record the sequence of rewards.  After running numerous events we should see the prediction accuracy of the model improve. 
# 

import datetime
import os
import json
# This will fail on the first import.  Just run it again and the error will disappear
import matplotlib.pyplot as plt
import random 
import requests
import time
import uuid
from pandas import DataFrame
from scipy import stats

### config constants 
VERBOSE = False
out_dir    = os.getcwd() + '/'        ## Default for -o option

# Replace 'personalization_base_url' and 'subscription_key' with your valid endpoint values.
endpoint = "https://westus2.api.cognitive.microsoft.com/"
personalization_base_url = endpoint # "http://localhost:5000"
subscription_key = "3a1ab38574454951a75eb7c9abfdd924" 




# Assemble the parts of the RESTFUL api calls. 
personalization_rank_url = personalization_base_url + "/personalizer/v1.0/rank"
personalization_reward_url = personalization_base_url + "/personalizer/v1.0/events/" #add "{eventId}/reward"
headers = {'Ocp-Apim-Subscription-Key' : subscription_key, 'Content-Type': 'application/json'}

examplepath = "example.json"
requestpath = "rankrequest.json"
actionfeaturespath = "actionfeatures.json"

random.seed(time.time())

userpref = None 
rankactionsjsonobj = None 
actionfeaturesobj = None

with open(examplepath) as handle:
    userpref = json.loads(handle.read())

with open(requestpath) as handle:
    rankactionsjsonobj = json.loads(handle.read())  
    
with open(actionfeaturespath) as handle:
    actionfeaturesobj = json.loads(handle.read())

########################################################################
def assemble_output_file_name(output_dir, prefix, suffix='.csv'):
    '''Place the file in the proper path, adding a prefix & suffix. eg.
    output_dir/sub_dir/prefix + index + suffix
    The output files will add a prefix & suffix to the date_index, e.g. ~/run/posteriors/regions_43.pkl '''
    ## Make sure the suffix starts with .
    if suffix[0] != '.':
        suffix = '.' + suffix
    ## Check if output dir exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print >> sys.stderr, 'Created:', output_dir
    ## Assemble the file name
    d = datetime.datetime.now()
    date_index = '-'.join([str(d) for d in d.timetuple()[0:6]])
    return os.path.join(output_dir, prefix + date_index + suffix)


def get_reward_from_simulated_data(name, weather, timeofday, prediction):
    '==1 if model prediction matches the persons choice, ==0 otherwise'
    if(userpref[name][weather][timeofday] == str(prediction)):
        return 1 
    return 0

def create_event_id(rankjsonobj):
    'Add a unique uuid to track the event.'
    eventid = uuid.uuid4().hex
    rankjsonobj["eventId"] = eventid
    return rankjsonobj, eventid

def add_random_features(rank_request):
    'Fill the request fields with random name, weather and timeofday features.'
    name = random.choice(namesopt)
    weather = random.choice(weatheropt)
    timeofday = random.choice(timeofdayopt)
    rank_request['contextFeatures'] = [{'timeofday': timeofday, 'weather': weather, 'name': name}]
    features = [name, weather, timeofday]
    return rank_request, features


def add_action_features(rank_request):
    'Fill the actions in the rank request.'
    rank_request["actions"] = actionfeaturesobj
    return rank_request


def summary_context(c_vector):
    'Moniker with the first letter of each context. To see the state at each step.'
    first_ltr = [str(k[0]) for k in c_vector]
    return ''.join(first_ltr)


# Reset the run data
recommendations = 0
reward = 0
rewards = []
count = []
icount = []
irewards = []
rankjsonobj = rankactionsjsonobj
    
namesopt = ['Alice', 'Bob', 'Cathy', 'Dave']
weatheropt = ['Sunny', 'Rainy', 'Snowy']
timeofdayopt = ['Morning', 'Afternoon', 'Evening']  # Or TRY a smaller state space. 


# The simulation loop. Running this could take a while :).  At first the HTTP service may be "cold"
# and return "500" errors.  Just try again and it should work. 
from time import clock
num_requests =  30 # 10000
start_t = clock()
last_count = 0
for i in range(num_requests):
      
    ## Fill in the rank-request object 
    #create unique id to associate with an event
    rankjsonobj, eventid = create_event_id(rankjsonobj)
    #generate random context
    rankjsonobj, features = add_random_features(rankjsonobj)
    [name, weather, timeofday] = features
    #add the actions to be ranked
    rankjsonobj = add_action_features(rankjsonobj)
    #Have the service choose an action
    response = requests.post(personalization_rank_url,
                             headers = headers,
                             params = None,
                             json = rankjsonobj)
    if response.status_code //  100 != 2:       # Must be in the 200s
        print(i, "\tBad context response: ", response.status_code)
        
    try:
        #compare personalization service recommendation with the simulated data to generate a reward value
        prediction = json.dumps(response.json()["rewardActionId"]).replace('"','')  # Extract the prediction from the response
        reward = get_reward_from_simulated_data(name, weather, timeofday, prediction)
    except:
        print(f"Response failed: {response.json()}")
        break
        
    #send the reward to the service 
    response = requests.post(personalization_reward_url + eventid + "/reward",
                             headers = headers,
                             params= None,
                             json = { "value" : reward })
    if response.status_code //  100 != 2:
        print(i, "\tBad reward response: ", response.status_code)
    #COmpute the sum of rewards for every 10 cycles 
    recommendations = recommendations + reward
    
    iplus = i + 1
    #wait (>1 min) between sending more events to observe learning in the next batch
    if(iplus % 500 == 0):
        print(f"Avg {sum(rewards[last_count:-1])/(count[-1]- count[last_count])} at {int(clock() - start_t)} secs.")
        last_count = len(count) -1
        time.sleep(20) 
             
    # Note event progress - the features and reward for every 10th event.
    if(iplus % 10 == 0): 
        print(summary_context( [name, weather, timeofday] ), ':{0:d} '.format(recommendations), sep='', end = ' ')
        rewards.append(recommendations)
        count.append(i)
        recommendations = 0

print("\nTotal of {}  rewards ".format(10* len(rewards)))


print("Avg reward: ",sum(rewards)/count[-1])

lm = stats.linregress(count, rewards)
y = [lm.slope * c + lm.intercept for c in count]
print("Percent change per event:{: .4f}%".format(100 * lm.slope))


csv_fn = assemble_output_file_name(out_dir, 'pers_data', suffix='.csv')
DataFrame(index=count, data=rewards, columns = ["rewards"]).to_csv(csv_fn)
# #### The learning rate
# 
# A postive rate of change implies learning improves recommendations over time. We see this by plotting the total number of correct recommendations for every batch of 10 events.


plt_fn = assemble_output_file_name(out_dir, 'pers_plot', suffix='.png')
plt.plot(count, rewards)
plt.plot(count, y, '-')
plt.xlabel("Batch of 10 rank events")
plt.ylabel("Correct recommendations per batch")
plt.title("Change in success rate over events.")
plt.savefig(plt_fn)
