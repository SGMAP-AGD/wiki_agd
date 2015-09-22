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

variables_a_garder['FRE_CODE_INSEE'] = variables_a_garder['AGEN']