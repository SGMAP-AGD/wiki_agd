# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 22:39:43 2015

@author: alexis
"""

import os
import pandas as pd

from wiki_agd.parser import create_model, create_model_from_table


path_csv = 'D://data//wiki//Cartographie_des_donnees_logement_-_2015-01-26.csv'

tab = pd.read_csv(path_csv, encoding='utf8')
tab = tab.iloc[:-1,:]

varnames = tab.columns.tolist()
varnames = ['table'] + tab.columns.tolist()[1:]
#tab.columns = ['table'] + varnames[1:4] + ['Origine', 'cond_acces', 'cout', ] +
tab.columns = varnames

def _write_description(row):
    text = row['Description'] + '\n\n'
    if row[u'Qualité des données'] != '':
        text += u'Éléments sur la qualité des données : \n' + row[u'Qualité des données'].lstrip() + '\n\n'
    if row[u'Remarques et perspectives éventuelles'] != '':
        text += 'Remarques et perspectives : \n' + row[u'Remarques et perspectives éventuelles'].lstrip() + '\n\n'
    return text


dic_text = dict(
                titre = u'table',
                producteur = u'Origine des données',
                gestionnaire = u'Gestionnaire',
                freq_maj = u'Fréquence',
                cond_acces = u"Conditions d'accès",
                cout = u"Coût d'accès",
                open_data = u'Données en open data',
                granul_geo = u'Granularité géographique',
                )

text = create_model_from_table(u'Jeu de données',
                               'logement',
                               tab,
                               'table',
                               _write_description,
                               dic_text)

path_doc = 'D://data//wiki'
path = os.path.join(path_doc, 'carto_log_wiki.txt')
with open(path, 'w+') as f:
    f.write(text.encode('utf8'))

# cd /git/pywikibot-core/scripts
#python pagefromfile.py -force -notitle -file:D:/data/wiki/carto_log_wiki.txt



