# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 22:39:43 2015

@author: alexis
"""


import pandas as pd

path_doc = 'D:/data/code_cnaf/tables_etalab.xls'

list_sheets = ['AGEN', 'FIL', 'GCA',
               'WEB', 'SDSUI']

variables_a_garder = dict()
for sheet in list_sheets:
    print sheet
    tab = pd.read_excel(path_doc, sheetname=sheet)
    variables_a_garder[sheet] = tab.Nom.tolist()


"""
Le dictionnaire tables_variables contient en clé toutes les variables présentes
 dans le dictionnaire variables_a_garder et en valeur une liste de toutes les
 tables dans lesquelles la variable est présente.

@author boupetch
"""
tables_variables = dict()

for table in variables_a_garder:
    for variable in variables_a_garder[table]:
        if variable in tables_variables:
            tables_variables[variable].append(table)
        else:
            tables_variables[variable] = [table]

for var, tables in tables_variables.iteritems():
    if len(tables) > 1:
        print(var, ' ', tables, '\n')


variables_a_garder['FRE_CODE_INSEE'] = variables_a_garder['AGEN']

