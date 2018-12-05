
# coding: utf-8

# In[5]:

from selenium import webdriver
import time
import re
from bs4 import BeautifulSoup
import requests


# open the website
driver = webdriver.PhantomJS(executable_path="phantomjs")
driver.get("http://split4.pmfst.hr/dadp/?a=list")
time.sleep(7)
web = driver.page_source
#print(web)
 
driver.close()

# make the source code in a formatted way
formatted = [] # a list with all elements with <>
for i in range(0,len(web)):
    if web[i] == '<':
        start = i
    if web[i] == '>':
        end = i
        formatted.append(web[start:end+1])
        
links = [] # all links to the peptide files

# find all links
for i in range(0,len(formatted)):
    element = re.findall(r"[.]([/][?]a=kartica&amp;id=SP_[^<>]*)\"",formatted[i])
    if element:
        links.append(element[0])
        
# full links
for i in range(0,len(links)):
    #print((links[i]))
    links[i] = 'http://split4.pmfst.hr/dadp'+links[i].replace('amp;','')
print(len(links))
    

# columns
entry = []
peptide_names = []
suborder = []
family = []
genus = []
species = []
ecozone = []
distribution = []
antimicrobial_and_other_activities = []
tissue = []
sequence = []
signal_peptide_class = []
signal = []
prepro = []
bioactive = []
bioactive_name = []
amidated = []
hc50 = []
mic_e_coli = []
mic_s_aureus = []



for i in range(0,len(links)):
    soup = BeautifulSoup(requests.get(links[i]).content,"html.parser")
    str_soup = str(soup)
    
    entry.append(re.findall("<td>Entry</td>\n<td>(.*)</td>",str_soup))

    peptide_names.append(re.findall("<td>Peptide names</td>\n<td>(.*)</td>",str_soup))

    suborder.append(re.findall("<td>Suborder</td>\n<td>(.*)</td>",str_soup))

    family.append(re.findall("<td>Family</td>\n<td>(.*)</td>",str_soup))

    genus.append(re.findall("<td>Genus</td>\n<td><i>(.*)</i></td>",str_soup))

    species.append(re.findall("<td>Species</td>\n<td><i>(.*)</i></td>",str_soup))
    
    ecozone.append(re.findall("<td>Ecozone</td>\n<td>(.*)</td>",str_soup))

    distribution.append(re.findall("<td>Distribution</td>\n<td>(.*)</td>",str_soup))
    
    antimicrobial_and_other_activities.append(re.findall("<td>Antimicrobial &amp; other activities</td>\n<td>(.*)</td>",str_soup))

    tissue.append(re.findall("<td>Tissue</td>\n<td>(.*)</td>",str_soup))

    raw_sequence = re.findall("<td>Sequence</td>\n<td><font\sface=\"Courier New\">([^\s]*)</font></td>",str_soup)
    raw_sequence[0] = raw_sequence[0].replace("<br/>",'')
    sequence.append(raw_sequence)
    
    signal_peptide_class.append(re.findall("<td>Signal peptide class</td>\n<td>(.*)</td>",str_soup))
    
    signal.append(re.findall("Signal</td>\n<td>\s</td>\n<td>.*</td>\n<td>\s</td>\n<td>([A-Z]*)</td>",str_soup))
    
    prepro.append(re.findall("<td>Prepro</td><td></td><td\swidth=\"10\">\d*</td><td\swidth=\"10\">\s</td><td>([A-Z]*)</td>",str_soup))
    
    bioactive.append(re.findall("<td>Bioactive</td><td>[^<>]*</td><td\swidth=\"10\">\d*</td><td\swidth=\"10\">[^<>]*</td><td>([A-Z]*)</td>",str_soup))
    
    bioactive_name.append(re.findall("<td>Bioactive</td><td>([^<>]*)</td>",str_soup))

    amidated.append(re.findall("<td>Bioactive</td><td>[^<>]*</td><td\swidth=\"10\">\d*</td><td\swidth=\"10\">([^<>]*)</td><td>[A-Z]*</td>",str_soup))
    
    hc50.append(re.findall("<td>Bioactive</td><td>[^<>]*</td><td\swidth=\"10\">\d*</td><td\swidth=\"10\">[^<>]*</td><td>[A-Z]*</td><td\salign=\"right\"\swidth=\"10\">([^<>]*)</td><td\salign=\"right\"\swidth=\"10\">[^<>]*</td><td\salign=\"right\"\swidth=\"10\">[^<>]*</td>",str_soup))
    
    mic_e_coli.append(re.findall("<td>Bioactive</td><td>[^<>]*</td><td\swidth=\"10\">\d*</td><td\swidth=\"10\">[^<>]*</td><td>[A-Z]*</td><td\salign=\"right\"\swidth=\"10\">[^<>]*</td><td\salign=\"right\"\swidth=\"10\">([^<>]*)</td><td\salign=\"right\"\swidth=\"10\">[^<>]*</td>",str_soup))
    
    mic_s_aureus.append(re.findall("<td>Bioactive</td><td>[^<>]*</td><td\swidth=\"10\">\d*</td><td\swidth=\"10\">[^<>]*</td><td>[A-Z]*</td><td\salign=\"right\"\swidth=\"10\">[^<>]*</td><td\salign=\"right\"\swidth=\"10\">[^<>]*</td><td\salign=\"right\"\swidth=\"10\">([^<>]*)</td>",str_soup))
    

    

        
        


# In[11]:

import pandas as pd
#data = pd.DataFrame
#entry_new = []+entry
# columns
entry_db = []
peptide_names_db = []
suborder_db = []
family_db = []
genus_db = []
species_db = []
ecozone_db = []
distribution_db = []
antimicrobial_and_other_activities_db = []
tissue_db = []
sequence_db = []
signal_peptide_class_db = []
signal_db = []
prepro_db = []
bioactive_db = []
bioactive_name_db = []
amidated_db = []
hc50_db = []
mic_e_coli_db = []
mic_s_aureus_db = []

for i in range(0,len(entry)):
    entry_db.append(entry[i][0])
    peptide_names_db.append(peptide_names[i][0])
    suborder_db.append(suborder[i][0])
    family_db.append(family[i][0])
    genus_db.append(genus[i][0])
    species_db.append(species[i][0])
    ecozone_db.append(ecozone[i][0])
    distribution_db.append(distribution[i][0])
    
    if antimicrobial_and_other_activities[i] != []:
        antimicrobial_and_other_activities_db.append(antimicrobial_and_other_activities[i][0])
    if antimicrobial_and_other_activities[i] == []:
        antimicrobial_and_other_activities_db.append('')
    
    tissue_db.append(tissue[i][0])
    
     
    if sequence[i] != []:
        sequence_db.append(sequence[i][0])
    if sequence[i] == []:
        sequence_db.append('')
    
    if signal_peptide_class[i] != []:
        signal_peptide_class_db.append(signal_peptide_class[i][0])
    if signal_peptide_class[i] == []:
        signal_peptide_class_db.append('')
        
    if signal[i] != []:
        signal_db.append(signal[i][0])
    if signal[i] == []:
        signal_db.append('')
        
    
    
    
    
    


# In[16]:

data = pd.DataFrame()

data['entry'] = entry_db
data['peptide_names'] = peptide_names_db
data['suborder'] = suborder_db
data['family'] = family_db
data['genus'] = genus_db
data['species'] = species_db
data['ecozone'] = ecozone_db
data['distribution'] = distribution_db
data['antimicrobial_and_other_activities'] = antimicrobial_and_other_activities_db
data['tissue'] = tissue_db
data['sequence'] = sequence_db
data['signal_peptide_class'] = signal_peptide_class_db
data['signal'] = signal_db
data['prepro'] = prepro
data['bioactive'] = bioactive
data['bioactive_name'] = bioactive_name
data['amidated'] = amidated
data['hc50'] = hc50
data['mic_e_coli'] = mic_e_coli
data['mic_s_aureus'] = mic_s_aureus


# In[36]:

#aaa = pd.read_csv("DADP.csv")
#print(aaa.iloc[217])

# replace all "&gt;" with '>'
for i in range(0,len(hc50)):
    for j in range(0,len(hc50[i])):
        hc50[i][j] = hc50[i][j].replace("&gt;",'>')

for i in range(0,len(mic_e_coli)):
    for j in range(0,len(mic_e_coli[i])):
        mic_e_coli[i][j] = mic_e_coli[i][j].replace("&gt;",'>')
        
for i in range(0,len(mic_s_aureus)):
    for j in range(0,len(mic_s_aureus[i])):
        mic_s_aureus[i][j] = mic_s_aureus[i][j].replace("&gt;",'>')
        
        
        
#aaa['hc50'][217] = '>150.00'
#print(aaa['hc50'][217])


# In[38]:

data['hc50'] = hc50
data['mic_e_coli'] = mic_e_coli
data['mic_s_aureus'] = mic_s_aureus


# In[40]:

data.to_csv("DADP_revised.csv", index=False)  #write data to csv file


# In[39]:

#print(data.iloc[217])

