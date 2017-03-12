
# coding: utf-8

# In[1]:

import urllib2
import sys
import re


# In[17]:

def find_position(ID):
    url = "https://www.ncbi.nlm.nih.gov/clinvar/" + ID

    link = urllib2.urlopen(url)
    read_link = link.read()

    init_table = read_link.find("<a target=\"_blank\" title=\"View in Variation Viewer\" href=")
    final_table = read_link.find("</a>", init_table)

    table = read_link[init_table:final_table]

    init_pos = table.find("Chr")
    final_pos = table.find("(",init_pos)

    pos = table[init_pos:final_pos]
    info = pos.split(":")

    if init_pos == -1:
        new_info = ["-","-"]
        return new_info
    else:
        return info


# In[15]:

infile = open(sys.argv[1])

for i in infile.readlines():
    result = find_position(i)
    print result[0], "\t", result[1]


# In[26]:




# In[22]:




# In[ ]:



