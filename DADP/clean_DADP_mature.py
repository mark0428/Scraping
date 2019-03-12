#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 15:21:01 2018

@author: cli

"""

"""
Derive all mature AMPs from DADP AMPs/precursors
"""

# In[]:
import pandas as pd
data = pd.read_csv('/projects/btl/cli/AMP_prediction_updated/data/AMP/DADP/DADP_all.csv')
print(data.head())

# In[]:
# 2571 original precursors+AMPs
bioactive = []
for i in range(len(data)):
    exec('temp =' + data.bioactive[i])
    bioactive.append(temp)
    
# In[]:
# output all bioactive as mature AMPs
# 3004 mature AMPs
mature = []
for i in range(len(bioactive)):
    for j in range(len(bioactive[i])):
        mature.append(bioactive[i][j])
        
# In[]:
# remove duplicates
# 1923 distinct mature AMPs
mature_cleaned = list(set(mature))

# In[]:
# write to fasta
ofile = open("/projects/btl/cli/AMP_prediction_updated/data/AMP/DADP/DADP_mature_AMP_20181206.fa", "w")

for i in range(len(mature_cleaned)):
    
    ofile.write(">" + "DADP" + str(i+1).zfill(4) + "\n" + mature_cleaned[i] + "\n")


ofile.close()