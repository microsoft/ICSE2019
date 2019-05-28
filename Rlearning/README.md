# Reinforcement Learning demos

Borrowed from
See http://pybrain.org/docs/tutorial/reinforcement-learning.html
 
To install the current pybrain 

```
    git clone https://github.com/pybrain/pybrain.git
    cd pybrain
    python3 setup.py install
```

### pybrain simulations:
    https://www.youtube.com/watch?v=fEM7YDNonSE

### Optimization in RL:
    http://pybrain.org/docs/tutorial/optimization.html#optimization-in-reinforcement-learning

## Running notebooks on the Azure Data Science Ubuntu VM

We work in the conda `py36` environment.  Enter this with the conda command:

```
    source activate py36
```
    
This environment needs to be setup to run jupyter notebooks by these installs:

```
    conda install jupyter
    conda install nb_conda
```

The following is not covered in the tutorial notebooks, but its here for reference:
## R install in Jupyter notebooks (careful - jupyter might not let you run python in this env)

    conda install -c r r-irkernel

#### Expose conda envs in jupyter - huh

    conda install nb_conda

## But this is also needed:

activate myenv
conda install ipykernel
python -m ipykernel install --user --name myenv

### Calling python from R:

https://rstudio.github.io/reticulate/articles/calling_python.html


### Source for Azure Personalizer notebook

https://github.com/Azure-Samples/cognitive-services-personalizer-samples

