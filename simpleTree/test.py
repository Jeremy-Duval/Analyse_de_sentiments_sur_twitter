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
"""
with open("dico", 'rb') as dictionary:
    depickler = pickle.Unpickler(dictionary)
    
    dictNP = depickler.load()

for row in dictNP.rowList:
    print("Mot : "+str(row.word)+"\n "+str(row.nbAppearPositive)+" - "+str(row.coefPositive)+"\n "+str(row.nbAppearNegative)+" - "+str(row.coefNegative))
"""

msg = ["J\'ai faim",
          "La vie est belle",
          "J\'aime les chats",
          "Je pense que excité",
          "Je suis aimé ! C'est beau !",
          "Ce n'est pas triste d'être joyeux"]
          
listWordMsg=oTree.lemnise(msg)

"""
for i in listWordMsg :
    for j in i :
        print(j)
"""
for i in listWordMsg:
    oTree.__calcCoefWithTree__(i)