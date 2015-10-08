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
