#!/usr/bin/python
# Jun 2019  JMA
# plot_progress.py  Style file for python modules
"""
Append sequential runs from the Personalizer RWRL demo to plot. 

Usage:
$ python ./plot_progress.py  [list of pers_data*.csv files]
""" 


### Python standard modules - remove those not necessary
# import copy
import math
import os
import os.path
import re
import string
# import subprocess
import sys
import time

import numpy as np
import pandas as pd
from scipy import stats

from bokeh.plotting import figure, show
#from bokeh.models.markers import Circle
from bokeh.colors.groups import blue
from bokeh.models import Label
from bokeh.layouts import column


### config constants 
VERBOSE = True
PLOT = True
plot_dir    = os.path.join(os.getcwd() , 'plots') #'ICSE2019/Rlearning/azure_personalizer/plots') ## Default for -o option

data_list = ("pers_data2019-6-26-5-28-25.csv",
"pers_data2019-6-26-5-46-13.csv",
"pers_data2019-6-26-6-3-56.csv",
"pers_data2019-6-26-6-21-36.csv",
"pers_data2019-6-26-6-39-26.csv",
"pers_data2019-6-26-18-29-52.csv",
"pers_data2019-6-26-18-47-40.csv",
"pers_data2019-6-26-19-5-41.csv",
"pers_data2019-6-26-23-43-9.csv",
"pers_data2019-6-27-0-0-41.csv",
"pers_data2019-6-27-16-26-39.csv",
"pers_data2019-6-27-16-44-2.csv",
"pers_data2019-6-27-16-9-8.csv",
"pers_data2019-6-27-17-1-38.csv")

########################################################################
def read_one(fn, group_index, the_df):
    if VERBOSE:
            print("Reading", fn, file=sys.stderr)
    next_df = pd.read_csv(os.path.join(os.getcwd(), fn), 
            names = ('count', 'reward'), 
            skiprows =1,
            index_col= False)
    next_df['group'] = group_index
    if the_df is None:
        the_df = next_df
    else:
        next_df['count'] = next_df['count'] + the_df['count'].values[-1]
        the_df = the_df.append(next_df)
    return the_df


########################################################################
if __name__ == '__main__':
    # Is there a cmd line arg for files to include? 
    if len(sys.argv) > 1:
        data_list = eval(sys.argv[1])
        if type(data_list) is not list:
            print("arg {} is not a list.".format(sys.argv[1]), file=sys.stderr)
            sys.exit(-1)
    # Just check that the file loads correctly
    reward_df = None
    index_offset = 0
    for k, a_file in enumerate(data_list):
        reward_df = read_one(a_file, k, reward_df)
    # print('Done!', '\n', reward_df.describe())
    if PLOT:
        p = figure(plot_width = 1000, plot_height = 320, 
        title = 'Learning curve',
        x_axis_label = 'events', y_axis_label = 'reward')
        grp_cnt = max(reward_df['group']) +1
        for grp in range(grp_cnt):
            segment = reward_df.loc[reward_df['group'] == grp]
            nrows = segment.shape[0]
            avg_reward = np.mean(segment['reward'].values)
            lm = stats.linregress(segment['count'], segment['reward'])
            print("{}: Percent change per event:{: .4f}%".format(grp, 100 * lm.slope))
            p.circle(segment['count'], segment['reward'].values + np.random.random((nrows))-0.5, size=2, alpha= 0.8, color = blue[grp % 15])
            p.line([min(segment['count'].values), max(segment['count'].values)], [avg_reward, avg_reward], color='black')
            annote = Label(x = min(segment['count'].values), y =8, 
                text= '{:.2f}:{:.3f}'.format(avg_reward, 100*lm.slope), 
                background_fill_color='WhiteSmoke', 
                text_font_size="8pt")
            p.add_layout(annote)
        show(p)
        print(segment.describe())
        print('Done!')
    else:
        reward_df.to_csv('reward.csv', index=False)
#EOF
