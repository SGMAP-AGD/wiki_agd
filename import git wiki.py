# -*- coding: utf-8 -*-
"""
Created on Mon Sep 07 20:23:03 2015

@author: alexis


Ce fichier a été construit pour importer le wiki construit dans le cadre de l'Open Damir
sur github dans le wiki de l'AGD.

"""

import os
import codecs

path_wiki = 'C:\git\DAMIR.wiki'

files = os.listdir(path_wiki)
files = [x for x in files if x[-3:] == '.md']
files.remove('_Sidebar.md')


def init_page(title):
    text = "{{-start-}} \n" + \
            "'''" + title + "'''" + "\n\n"
    return text.decode('utf8')


def bas_de_page():
    text = '\n \nCette page a été générée par un robot \n\n[[Category:CNAMTS]]\n{{-stop-}} \n \n'
    return text.decode('utf8')


def fill_model(name):
    # TODO: dict to translate format into type
    text = """
{{Variable
|nom= """ + name + """
|table= OpenDamir
|type= """ + """
|format=
}}

"""
    return text.decode('utf8')

debut_table = """{| class=\"wikitable\"
! scope=\"col\" | Code
! scope=\"col\" | Label
"""


def start_wikitable(title_markdown):
    line = title_markdown[2:-2]
    parts = line.split('|')
    assert len(parts)
    debut_table = """{| class=\"wikitable\"
! scope=\"col\" | Code
! scope=\"col\" | Label
"""
#    import pdb; pdb.set_trace()
    return debut_table


all_pages = ''
total_text = ''
for page in files:
    path = os.path.join(path_wiki, page)
    name = page[:-3].decode('cp1252').encode('utf8')
    with codecs.open(path, encoding='utf8') as f:
        text = f.read()
        text_by_line = text.split('\r\n')
        if text_by_line[-1] == '':
            text_by_line = text_by_line[:-1]
        if u'|----|----|' in text_by_line:
            ligne_start_table = text_by_line.index(u'|----|----|') - 1
            # on récupère le label qui peut servir de définition:
            title_markdown = text_by_line[ligne_start_table][2:-2]
            label = title_markdown.split('|')[1]
            # on marque le début du tableau
            text_by_line[ligne_start_table] = debut_table
            #on repère et on marque la fin du tableau
            if text_by_line[-1][-1] == '|':
                text_by_line.append('|}')
            elif text_by_line[-2][-1] == '|':
                text_by_line.insert(-1, '|}')
            else:
                for k in range(ligne_start_table + 1, len(text_by_line) - 1):
                    if text_by_line[k] == text_by_line[k + 1] == '':
                        ligne_start_table = k
                        text_by_line.insert(k, '|}')
                        break
                if k == len(text_by_line) - 2:
                    import pdb; pdb.set_trace()

            text_by_line = [label, ''] + text_by_line
            text = '\r\n'.join(text_by_line)


    total_text += init_page(name) + fill_model(name) + text + bas_de_page()

    all_pages += '[[' + name + ']]'



file_to_wiki = os.path.join(path_wiki, 'damir_wiki.txt')
with open(file_to_wiki, 'w+') as f:
    f.write(total_text.encode('utf8'))

file_to_delete = os.path.join(path_wiki, 'damir_pages.txt')
with open(file_to_delete, 'w+') as f:
    f.write(all_pages)




