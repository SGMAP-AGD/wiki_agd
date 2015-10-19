# -*- coding: utf-8 -*-
"""
Created on Thu Oct 08 21:39:35 2015

@author: Alexis
"""


def init_page(title):
    text = "{{-start-}} \n" + \
            "'''" + title + "'''"
    return text


def init_table():
    return """{| class=\"wikitable\"
! scope=\"col\" | Code
! scope=\"col\" | Label """


def bas_de_page(category):
    text = 'Cette page a été initialement générée par un robot \n\n'
    if category != '':
        text += '[[Category:' + category + ']]'
    text += '\n{{-stop-}} \n \n'
    return text.decode('utf8')


def create_model(name_model, **kwargs):
    text_model = '{{' + name_model + '\n'
    for param, value in kwargs.iteritems():
        text_param = '|' + param + ' = ' + value + '\n'
        text_model += text_param
    text_model += '}}'
    return text_model


def create_model_from_table(model, category, table, name_varname, _write_description,
                            dic_model_parameter_by_var):
    tab = table.fillna('')
    text_total = ''
    for _, row in tab.iterrows():
        text_row = init_page(row[name_varname]) + '\n\n'
        # dict for the row
        dict_for_the_row = dict()
        for key, value in dic_model_parameter_by_var.iteritems():
            dict_for_the_row[key] = row[value]

        dict_for_the_row[u'thème'] = category
        dict_for_the_row['description'] = _write_description(row)

        text_row += create_model(model, **dict_for_the_row) + '\n\n'
        text_row += bas_de_page(category)
        text_total += text_row
    return text_total



