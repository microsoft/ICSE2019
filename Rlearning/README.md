# Reinforcement Learning demos


## Running notebooks on the Azure Data Science Ubuntu VM

These demos are borrowed from
http://pybrain.org/docs/tutorial/reinforcement-learning.html
 
### Setting up your python environment

Here's how to set up your local windows machine to run the demo notebooks. We use "miniconda" python, installable from http://anaconda.org. 
We will work in our conda `python36` environment in which we do the pybrain install. `conda` has just been upgraded to work with powershell. You'll need to run the upgrade with administrator priviledges to get the most recent version:

    c:> conda  upgrade conda
    [...]
    c:> conda --version
    conda 4.6.14

Then, to set up powershell run

    c:> conda init powershell

You will then be able to choose environments in powershell simply by

    (base) PS> conda activate python36
    (python36) PS>


These packages need to be setup in your environment to run jupyter notebook:

```
    (python36) PS> conda install jupyter
    (python36) PS> conda install nb_conda     # Expose conda envs in jupyter
    (python36) PS> conda install matplotlib

    (python36) PS> conda install ipykernel
    (python36) PS> python -m ipykernel install --user --name python36 
```

### pybrain install

To install the current pybrain, you should clone it in your python version 3.6 environment:

```
    git clone https://github.com/pybrain/pybrain.git
    cd pybrain
    python3 setup.py install
```

### pybrain simulations:
    https://www.youtube.com/watch?v=fEM7YDNonSE

### Optimization in RL:
    http://pybrain.org/docs/tutorial/optimization.html#optimization-in-reinforcement-learning

The following is not covered in the tutorial notebooks, but its here for reference:

## R install in Jupyter notebooks (careful - jupyter might not let you run python in this env)

    conda install -c r r-irkernel


### Calling python from R:

https://rstudio.github.io/reticulate/articles/calling_python.html


### Source for Azure Personalizer notebook

https://github.com/Azure-Samples/cognitive-services-personalizer-samples

