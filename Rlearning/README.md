# Reinforcement Learning demos

Borrowed from
# See http://pybrain.org/docs/tutorial/reinforcement-learning.html
# 
# To install the current pybrain 
# git clone https://github.com/pybrain/pybrain.git
# cd pybrain
#sudo python3 setup.py install
# See https://github.com/pybrain/pybrain/issues/211
#
# Using python 3.6.5, 
# simpy.__version__ == 3.0.10 
# For simpy compatibility, change "expm2" to "expm" in
# C:\ProgramData\Miniconda3\envs\simpy\lib\site-packages\pybrain\tools\functions.py
#
# pybrain simulations:
# https://www.youtube.com/watch?v=fEM7YDNonSE

# Optimization in RL:
# http://pybrain.org/docs/tutorial/optimization.html#optimization-in-reinforcement-learning


# python debug:
# https://insights.dice.com/2019/05/22/python-debugging-improve-skills/
# McGill student M. Ghamsari "Python based RL, AI and NN library"
# https://www.youtube.com/watch?v=thAHR3_nj8E&list=PLnZEPpH20YVZe9z4KWPJOkBCvo03yJu9E&index=2&t=0s

import numpy as np

## R install in Jupyter notebooks (careful - jupyter might not let you run python in this env)

    conda install -c r r-irkernel

## Expose conda envs in jupyter - huh

    conda install nb_conda

## But this is also needed:

activate myenv
conda install ipykernel
python -m ipykernel install --user --name myenv



Calling python from R:

https://rstudio.github.io/reticulate/articles/calling_python.html


Source for Azure Personalizer notebook

https://github.com/Azure-Samples/cognitive-services-personalizer-samples

