# ICSE Tutorial on Scalable Data Science with Python and R

## Setup instructions

### Prerequisites

You will need an Azure subscription. You can get a free trial subscription, as described below. 
It takes about 3 minutes and will require a credit card, which is only required to verify your identity. The subscription comes with $200 credit 
and your credit card will not be charged unless you actively initiate an upgrade. 

1. Create a Microsoft account at https://outlook.com (skip if you already have an account @outlook.com, @Hotmail.com, or @live.com)
2. Use your Microsoft account to get the free Azure subscription https://azure.microsoft.com/en-us/free/
  * You get 200$ Azure credits expiring in 30 days
  * Credit card needed for identification purpose. You will not be charged even after  30 days or the 200$ credits are used
3. Create an Ubuntu Linux DSVM https://docs.microsoft.com/en-us/azure/machine-learning/data-science-virtual-machine/dsvm-ubuntu-intro
4. Create an AzureML workspace https://docs.microsoft.com/en-us/azure/machine-learning/service/setup-create-workspace#portal
5. Install x2go client on your local machine https://wiki.x2go.org/doku.php/doc:installation:x2goclient
6. Test connecting to your DSVM
  * Go to Azure portal to get the public IP of your DSVM
  * Connect to it from x2go client by choosing XFCE
  * After connecting, open a command window and clone the github repository to get the tutorial content to your DSVM: git clone https://github.com/microsoft/ICSE2019

Alternate prerequisites to run these examples locally on your machine:
* Your favorite git client. The original is [here](https://git-scm.com/downloads).
* A distribution of Python 3: [Anaconda](https://www.anaconda.com/distribution/) works well. (5 minutes on good network)
* A distribution of R: How about [Microsoft R Open](https://mran.microsoft.com/open)? (2 minutes on good network)

## Introduction to Machine Learning at Scale

## Introduction to Scalable R

## R on Spark hands-on

1. Launch X2go Client and click Session | New Session
  * Host: enter host IP address
  * Login: enter username
  * Session type: choose XFCE
  * Click OK
  * Click the icon or the session name, e.g. “New session”
  * Enter password
  * Click OK
2. Open command window on DSVM and execute “docker run” command:
  * sudo docker run -e PASSWORD=mypassword1 -p 8787:8787 rocker/verse
3. Open web browser on DSVM and connect to RStudio Server on port 8787:
  * http://localhost:8787
  * username: rstudio
  * password: mypassword1
4. Open terminal window in RStudio and clone git repo
  * git clone https://github.com/microsoft/ICSE2019
5. In the Files pane in RStudio,
  * Open the ICSE2019 folder
  * Open the R folder
  * Click 1-Intro-Transform-Train-Score.Rmd (not the .nb.html file) to open the first hands-on script
  * When it says that certain packages are required but are not installed, click “Install”
  * Click 2-ML-Pipelines.Rmd (not the .nb.html file) to open the second hands-on script
  * When it says that certain packages are required but are not installed, click “Install”

## Automated ML

AutomatedML takes care of the repetitive process of hypothesizing a model, fitting it to the data,
evaluating, and repeating until alternatives or the data scientist have been exhausted. It can
run locally or use the power of the cloud to try many models in parallel.

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

### Setup steps - Automated ML
* Clone the [Machine Learning Notebooks repo](https://github.com/Azure/MachineLearningNotebooks).
* Open a shell or command prompt window, go to `/how-to-use-azureml/automated-machine-learning` and execute the `automl_setup` script appropriate for your platform (Win, Linux, Mac). Many packages will be installed (10 minutes on good network).
* A browser window with Jupyter will open. Ctrl+C the ipykernel in the terminal.
* Re-start jupyter in the root directory of the repo (two folders up) with `jupyter notebook`
* Open the setup notebook [configuration.ipynb](https://github.com/Azure/MachineLearningNotebooks/blob/master/configuration.ipynb).
* Make sure to use the `azure_automl` kernel.
* Transfer your subscription information and resource group name into the second code cell of the notebook.
* Run cells according to instructions. 

## Reinforcement Learning

This will be a presentation interspersed with 3 notebook demos.  The notebooks are available in the Rlearn subdirectory of this repository. Note that all demos were developed using python version 3.6  - available on the DSVM as `source activate py36`.

* To run the two "Maze" demos you will need to install the current `pybrain` from github, by running:

```
    git clone https://github.com/pybrain/pybrain.git
    cd pybrain
    python3 setup.py install
```

You may need to `conda install setuptools` for this to work.  
 
Other dependencies on numpy, scipy and matplot lib should already by installed on the Data Science VM.

* To run the Azure Personalizer you need to creae a Personalizer(preview) resource in Azure, from which you can find the resource key and URL endpoints to be incorporated in your script for running the resource.

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
