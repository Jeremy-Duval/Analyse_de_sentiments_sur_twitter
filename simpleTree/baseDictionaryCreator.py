# -*- coding: utf-8 -*-
"""
Create the base dictionary.

Created on Tue Mar 13 16:54:56 2018

@author: jeremy
"""
from DictionaryRow import DictionaryRow
import pickle


row = DictionaryRow()

with open('dico.txt', 'wb') as dictionary:
    pickler = pickle.Pickler(dictionary)
    
    row.word = "joyeux"
    row.nbAppearance = 1
    row.coefPositive = 1.0
    row.coefNegative = None
    pickler.dump(row)#save the row
    
    row.word = "triste"
    row.nbAppearance = 1
    row.coefPositive = None
    row.coefNegative = 1.0
    pickler.dump(row)#save the row
    
    row.word = "exité"
    row.nbAppearance = 1
    row.coefPositive = 1.0
    row.coefNegative = 1.0
    pickler.dump(row)#save the row
    
    row.word = "anxieux"
    row.nbAppearance = 1
    row.coefPositive = None
    row.coefNegative = 1.0
    pickler.dump(row)#save the row
    
    row.word = "heureux"
    row.nbAppearance = 1
    row.coefPositive = 1.0
    row.coefNegative = None
    pickler.dump(row)#save the row