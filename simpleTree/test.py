# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 11:58:43 2018

@author: jeremy
"""
import pickle
from OurTree import *
from DictionaryRow import DictionaryRow
from DictionaryNP import DictionaryNP


oTree = OurTree()

with open("dico", 'rb') as dictionary:
    depickler = pickle.Unpickler(dictionary)
    
    dictNP = depickler.load()
    
for row in dictNP.rowList:
    print(row.word)