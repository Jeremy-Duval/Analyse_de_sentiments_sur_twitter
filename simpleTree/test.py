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
          
msg2 = ["Vive les patates !",
        "J'aime les frites !",
        "Les chats sont beau et joyeux, je les aimes !"]
          
listWordMsg=oTree.lemnise(msg)

"""
for i in listWordMsg :
    for j in i :
        print(j)
"""
coefList = oTree.lemToCoef(listWordMsg)
print(coefList)
coef = oTree.calculateCoef(coefList)
print(coef)
"""
coefList2 = oTree.lemToCoef(oTree.lemnise(msg2))
coef = oTree.actualizeCoef(coef, 6, coefList2)
print(coef)
"""