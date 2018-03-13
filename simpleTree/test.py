# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 11:58:43 2018

@author: jeremy
"""
import pickle
from OurTree import *


oTree = OurTree()

with open("dico.txt", 'rb') as dictionary:
    depickler = pickle.Unpickler(dictionary)
    row = depickler.load()
    print(row.word)
    row = depickler.load() #nead to read next
    print(row.word)