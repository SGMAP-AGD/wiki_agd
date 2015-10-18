# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 21:51:31 2015

@author: alexis
"""

import os
import pandas as pd

from parser import init_page, init_table, bas_de_page, create_model


path_doc = 'D:/data/code_cnaf/'


def code_to_wikitable(code):
    if code == '':
        return ''
    table = code[3:].replace('\r\n', '\n|- \n|')
    table = '|- \n|' + table.replace('\t', ' || ') + '\n'
    text = table + '|}'
    return text


def fill_model(row, filename):
    # TODO: dict to translate format into type
    text = """
{{Variable
|nom= """ + row['nom_var_raccourci'] + """
|table= """ + filename + """
|type= """ + """
|format= """ + "\n }}"
    return text

def fill_model(row, filename):
   create_model('Variable',
                nom = row['nom_var_raccourci'], 
                table = filename,
                type = '',
                format = '')
    return text
    



def generate_texts_pywikibot(feuille, filename, variables_a_garder=None):
    ''' genere le fichier texte utilisé ensuite par pyikibot
        - variables_a_garder permet de selectionner une variable par fichier d'entrée
        - filename est le nom du fichier de destination
    '''

    feuille = feuille[feuille.nom_var.notnull()]
    feuille.fillna('', inplace=True)

    if translation is None:
        filename_dest = filename
    else:
        filename_dest = translation[filename]

    if variables_a_garder is None:
        var_to_keep = feuille['nom_var_raccourci'].tolist()
    else:
        var_to_keep = variables_a_garder[filename_dest]
    feuille = feuille[feuille['nom_var_raccourci'].isin(var_to_keep)]

    text = ''
#    feuille = feuille.iloc[:6, :]
    for _, row in feuille.iterrows():
        text_page = init_page(row['nom_var_raccourci']) + '\n'
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

#xxxx
#'''Nom de la page'''
#Texte ici
#
#yyyy
#xxxx
#'''Nom d'une autre page'''
#Un autre texte
#yyyy

if __name__ == '__main__':

    translation = dict(
        wbcontac = 'WEB',
        glsdp010 = 'SDSUI',
        glgc0020 = 'GCA',
        fi001000 = 'FIL',
        allaah = 'AGEN',
        allpaje = 'AGEN',
        allcommu = 'AGEN',
        alldatam = 'AGEN',
        allenf = 'AGEN',
        alloheix = 'AGEN',
        allrsa = 'AGEN',
        )

#    for filename in ['wbcontac', 'glsdp010',
#                     'fi001000',
#                     'allaah', 'allpaje','glgc0020'
#                     ]:
#        file = os.path.join(path_doc, filename)
#        feuille = pd.read_csv(file + '.csv', sep=';', encoding='utf8')
#         generate_text_pywikibot(feuille, filename)
    from wiki_agd.CNAF.read_excel import variables_a_garder

    dico_des_texts = dict()
    variables_retenues = ''
    for filename_dest in translation.values():
        dico_des_texts[filename_dest] = ''

    for filename, filename_dest in translation.iteritems():
        file = os.path.join(path_doc, filename)
        feuille = pd.read_csv(file + '.csv', sep=';', encoding='utf8')
        text, to_delete = generate_texts_pywikibot(feuille, filename, variables_a_garder)
        dico_des_texts[filename_dest] += text
        variables_retenues += ' ' + to_delete

    for filename_dest in set(translation.values()):
        path = os.path.join(path_doc, filename_dest + '_wiki.txt')
        with open(path, 'w+') as f:
            f.write(dico_des_texts[filename_dest].encode('utf8'))
        #utile pour les copier coller ensuite
        print 'python pagefromfile.py -notitle -file:' + path

    path = os.path.join(path_doc, 'delete_wiki.txt')
    with open(path, 'w+') as f:
        f.write(variables_retenues.encode('utf8'))


path = os.path.join(path_doc, 'delete_wiki.txt')
# cd /git/pywikibot-core/scripts
#python pagefromfile.py -force -notitle -file:D:/data/code_cnaf/fi001000_wiki.txt
#python pagefromfile.py -notitle -file:D:/data/code_cnaf/fi001000_wiki.txt