# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 11:58:43 2018
@author: jeremy
"""
#Importations nécessaires pour utiliser notre arbre (attention : prendre en compte que le fichier test se trouve dans le même dossier que les autres classes)
import pickle
from OurTree import *
from DictionaryRow import DictionaryRow
from DictionaryNP import DictionaryNP

#Ci-dessous on affiche juste chaque row du dico
with open("dico", 'rb') as dictionary:
    depickler = pickle.Unpickler(dictionary)
    
    dictNP = depickler.load()

for row in dictNP.rowList:
    print("Mot : "+str(row.word)+"\n "+str(row.nbAppearPositive)+" - "+str(row.coefPositive)+"\n "+str(row.nbAppearNegative)+" - "+str(row.coefNegative))


