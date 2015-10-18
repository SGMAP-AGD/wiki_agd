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


def bas_de_page():
    return 'Cette page a été initialement générée par un robot \n\n[[Category:CNAF]]\n{{-stop-}} \n \n'.decode('utf8')


def create_model(name_model, **kwargs):
    text_model = '{{' + name_model + '\n'
    for param, value in kwargs.iteritems():
        text_param = '|' + param + ' = ' + value + '\n'
        text_model += text_param
    text_model += '}}'
    return text_model
    
def create_model_from_table(model, table, name_varname, dic_model_parameter_by_var):
    text_total = ''
    for _, row in table.iloc[:,:5].iterrows():
        text_row = init_page(row[name_varname])
        # dict for the row
        dict_for_the_row= dict()       
        for key, value in dic_model_parameter_by_var.iteritems():
            dict_for_the_row[key] = row[value]
        text_row += create_model(model, **dict_for_the_row)
        text_row += bas_de_page()
        text_total += text_row
    return text_total
        
    
    
