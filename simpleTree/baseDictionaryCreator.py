# -*- coding: utf-8 -*-
"""
Create the base dictionary.

Created on Tue Mar 13 16:54:56 2018

@author: jeremy
"""
from DictionaryRow import DictionaryRow
from DictionaryNP import DictionaryNP
import pickle


dictNP = DictionaryNP()

with open('dico', 'wb') as dictionary:
    pickler = pickle.Pickler(dictionary, -1)
    #add rows
    dictNP.append(DictionaryRow("joyeux",1.0, None))
    dictNP.append(DictionaryRow("triste",None,1.0))
    dictNP.append(DictionaryRow("excité",1.0,1.0))
    dictNP.append(DictionaryRow("anxieux",None,1.0))
    dictNP.append(DictionaryRow("heureux",1.0,None))
    #save the dictionary in file
    pickler.dump(dictNP)