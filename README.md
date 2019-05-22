# ICSE Tutorial on Scalable Data Science with Python and R

## Setup instructions

### Prerequisites

To run these examples locally on your machine, you will need this basic software:
* Your favorite git client. The original is [here](https://git-scm.com/downloads).
* A distribution of Python 3: [Anaconda](https://www.anaconda.com/distribution/) works well. (10 minutes on good network)

You will also need an Azure subscription. You can [get a free one](https://azure.microsoft.com/en-us/free/).
It takes about 3 minutes and will require a credit card, which is only required to verify your identity.
(No free Azure resources for spam and other darlings.) The subscription comes with free credit 
and your credit card will not be charged unless you initiate an upgrade and rack up *a lot* of compute charges. 

### Setup steps - Automated ML locally on your laptop
* Clone the [Machine Learning Notebooks repo](https://github.com/Azure/MachineLearningNotebooks).
* Open a shell or command prompt window, go to `/how-to-use-azureml/automated-machine-learning` and execute the `automl_setup` script appropriate for your platform (Win, Linux, Mac). Many packages will be installed (10 minutes on good network).
* A browser window with Jupyter will open. You might need to re-start jupyter in the root directory of the repo.
* Execute the setup notebook [configuration.ipynb](https://github.com/Azure/MachineLearningNotebooks/blob/master/configuration.ipynb).  

## Introduction to Machine Learning at Scale

## AutoML on Azure ML Services

## Introduction to Scalable R

## R on Spark hands-on

## Reinforcement Learning Demo

## Automated ML

If you brought a nice, clean dataset, please feel free to try the notebooks on it if you complete
them before the guy on the podium does! If you brought an big, ugly, hairy, real one, let's talk
after the tutorial.

The approximate content of this demonstration will be:

* Configuration (notebook)
* AzureML basics (slides, hands-on playtime)
* Automated ML basics (slides, hands-on playtime)
* A simple classification problem
* Creating and attaching scalable compute, managing it in the Portal
* AutomatedML user interface in Portal
* AutomatedML forecasting
* Deploying AutomatedML models


### Contributing

Contact us if you'd like to contribute to this repository.

Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.microsoft.com.

When you submit a pull request, a CLA-bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., label, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.
