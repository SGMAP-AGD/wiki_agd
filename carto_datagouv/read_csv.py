# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 22:39:43 2015

@author: alexis
"""

import os
import pandas as pd

from wiki_agd.parser import create_model, create_model_from_table


path_csv = 'M://data//Cartographie_des_donnees_logement_-_2015-01-26.csv'

tab = pd.read_csv(path_csv)
tab.columns = ['table'] + tab.columns.tolist()[1:]


def get_description(row):
    text = ''

    return text    

row = tab.iloc[0,:]


text = create_model('Jeu de données',
                    titre = row['table'],
                    producteur = row['Origine des données'],
                    gestionnaire = row['Gestionnaire'],
                    freq_maj = row['Fréquence']
                    )
#TODO : to be continued
print text

dic_text = dict(
                titre = u'table',
                producteur = u'Origine des données',
                gestionnaire = u'Gestionnaire',
                freq_maj = u'Fréquence'
                )
text = create_model_from_table('Jeu de données',
                               tab,
                               'table',
                               dic_text)
print text

xxx

def generate_texts_pywikibot(tab):
    ''' genere le fichier texte utilisé ensuite par pyikibot '''
    text = ''
#    feuille = feuille.iloc[:6, :]
    for _, row in tab.iterrows():
        import pdb; pdb.set_trace()
        text_page = init_page(row[u'table']) + '\n'
        descr = row['Description']
        if descr[0] == ' ':
            descr = descr[1:]
        text_page += descr + '\n \n'
        text_page += fill_model(row, filename_dest) + '\n \n'
        if row['Codification'] != '':
            text_page += init_table() + '\n'
            text_page += code_to_wikitable(row['Codification']) + '\n \n'
        text_page += bas_de_page()
        text += text_page


    to_delete = feuille['nom_var_raccourci']
    list_to_delete = ('[[CNAF:' + to_delete + ']]').tolist()
    text_to_delete = ' '.join(list_to_delete)

    return text, text_to_delete

