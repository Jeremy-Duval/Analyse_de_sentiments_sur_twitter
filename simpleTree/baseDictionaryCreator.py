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
    dictNP.append(DictionaryRow("excite",1.0,1.0))
    dictNP.append(DictionaryRow("anxieux",None,1.0))
    dictNP.append(DictionaryRow("heureux",1.0,None))
    dictNP.append(DictionaryRow("aimer",1.0,None))
    dictNP.append(DictionaryRow("detester",None,1.0))
    dictNP.append(DictionaryRow("pauvre",None,1.0))
    dictNP.append(DictionaryRow("malade",None,1.0))
    dictNP.append(DictionaryRow("juste",1.0,None))
    dictNP.append(DictionaryRow("tranquille",1.0,None))
    dictNP.append(DictionaryRow("gentil",1.0,None))
    dictNP.append(DictionaryRow("mauvais",None,1.0))
    dictNP.append(DictionaryRow("meilleur",1.0,1.0))
    dictNP.append(DictionaryRow("fort",1.0,None))
    dictNP.append(DictionaryRow("faible",None,1.0))
    dictNP.append(DictionaryRow("gagner",1.0,None))
    dictNP.append(DictionaryRow("perdre",None,1.0))
    dictNP.append(DictionaryRow("mignon",1.0,None))
    dictNP.append(DictionaryRow("moche",None,1.0))
    dictNP.append(DictionaryRow("laid",None,1.0))
    dictNP.append(DictionaryRow("beau",1.0,None))
    dictNP.append(DictionaryRow("prefere",1.0,None))
    #save the dictionary in file
    pickler.dump(dictNP)