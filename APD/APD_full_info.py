#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 13:21:01 2018

@author: cli
"""

# In[]:
from selenium import webdriver
import time
import re
from bs4 import BeautifulSoup
import requests


# find all links
links = []
for i in range(1,3043):
    links.append('http://aps.unmc.edu/AP/database/query_output.php?ID='+'%05d'%i)

# In[]:
APD_ID = []
Name_Class = []
#Source = []
Sequence = []
Length = []
Net_charge = []
Hydrophobic_residue_percentage = []
Boman_Index = []
Three_D_Structure = []
#Method = []
#SwissProt_ID = []
Activity = []
#Crucial_residues = []
#Additional_info = []
#Title = []
#Author = []
#Reference = []

for i in range(len(links)):
    soup = BeautifulSoup(requests.get(links[i]).content,"html.parser")
    str_soup = str(soup)
    APD_ID.append((re.findall("APD ID:</p></td>\n<td width=\"61%\"><p>(.*)</p></td>",str_soup))[0])
    Name_Class.append((re.findall("Name/Class:</p></td>\n<td width=\"61%\"><p>(.*)</p></td>\n",str_soup))[0])
    #Source.append((re.findall("Name/Class:</p></td>\n<td width=\"61%\"><p>(.*)</p></td>",str_soup))[0])
    Sequence.append((re.findall("Sequence:</p></td>\n<td width=\"61%\"><p><font color=\"#ff3300\">(.*)</font></p></td>\n",str_soup))[0])
    Length.append((re.findall("Length:</p></td>\n<td width=\"61%\"><p>(.*)</p></td>\n",str_soup))[0])
    Net_charge.append((re.findall("Net charge:</p></td>\n<td width=\"61%\"><p>(.*)</p></td>\n",str_soup))[0])
    Hydrophobic_residue_percentage.append((re.findall("Hydrophobic residue%:</p></td>\n<td width=\"61%\"><p>(.*)</p></td>\n",str_soup))[0])
    Boman_Index.append((re.findall("Boman Index:</p></td>\n<td width=\"61%\"><p>(.*)</p></td>\n",str_soup))[0])
    Three_D_Structure.append((re.findall("3D Structure:</p></td>\n<td width=\"61%\"><p>(.*)</p></td>\n",str_soup))[0])
    Activity.append((re.findall("Activity:</p></td>\n<td width=\"61%\"><p>(.*)</p></td>\n",str_soup))[0])


# In[]:
# write to csv
import pandas as pd
data = pd.DataFrame()
data['APD_ID'] = APD_ID
data['Name/Class'] = Name_Class
data['Sequence'] = Sequence
data['Length'] = Length
data['Net_charge'] = Net_charge
data['Hydrophobic_residue_percentage'] = Hydrophobic_residue_percentage
data['Boman_Index'] = Boman_Index
data['Three_D_Structure'] = Three_D_Structure
data['Activity'] = Activity

data.to_csv('/projects/btl/cli/AMP_prediction_updated/data/AMP/APD/APD_full_20181207.csv', index=False)