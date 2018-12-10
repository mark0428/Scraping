#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 14:22:45 2018

@author: cli
"""

# clean APD and write into fasta
# In[]:

import pandas as pd
data = pd.read_csv('/projects/btl/cli/AMP_prediction_updated/data/AMP/APD/APD_full_20181207.csv')
print(data.head())

# In[]:
APD_mature = list(set(data.Sequence))

# In[]:
ofile = open("/projects/btl/cli/AMP_prediction_updated/data/AMP/APD/APD_mature_AMP_20181207.fa", "w")

for i in range(len(APD_mature)):
    
    ofile.write(">" + "APD" + str(i+1).zfill(4) + "\n" + APD_mature[i] + "\n")


ofile.close()