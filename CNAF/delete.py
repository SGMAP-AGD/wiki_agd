# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 14:23:40 2015

@author: User
"""

import os
import re
import pdb
import pandas as pd
from os.path import join


path_doc = 'D:/data/code_cnaf/'

filename = 'fi001000'

file = os.path.join(path_doc, filename)
feuille = pd.read_csv(file + '.csv', sep=';', encoding='utf8')
feuille = feuille[feuille.nom_var.notnull()]
feuille.fillna('', inplace=True)

to_delete = feuille['nom_var_raccourci'].iloc[:2]

list_to_delete = ('[[CNAF:' + to_delete + ']]').tolist()
text = ' '.join(list_to_delete)

path = os.path.join(path_doc, 'delete_wiki.txt')
f = open(path, 'w+')
f.write(text)
f.close()

# cd /git/pywikibot-core/scripts
#python delete.py -file:D:/data/code_cnaf/delete_wiki.txt
