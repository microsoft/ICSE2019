#!/usr/bin/python
# Jun 2019  JMA
# plot_progress.py  Style file for python modules
"""
Append sequential runs from the Personalizer RWRL demo to plot. 

Usage:
$ python ./plot_progress.py
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

from bokeh.plotting import figure, show
from bokeh.layouts import column


### config constants 
VERBOSE = True
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
    next_df = pd.read_csv(os.path.join(plot_dir, fn), 
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
    # Just check that the file loads correctly
    reward_df = None
    index_offset = 0
    for k, a_file in enumerate(data_list):
        reward_df = read_one(a_file, k, reward_df)
    print('Done!', '\n', reward_df.describe())
    reward_df.to_csv('reward.csv', index=False)
#EOF
