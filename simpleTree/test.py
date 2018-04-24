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

#Creation de notre arbre
oTree = OurTree()

#Liste de tweets artificiels pour le test
msg = ["J\'ai faim",
          "La vie est belle",
          "J\'aime les chats",
          "Tellement plaisant d\'être au soleil",
          "Je suis aimé ! C'est beau !",
          "Ce n'est pas triste d'être joyeux"]
#2e liste     
msg2 = ["Vive les patates !",
        "J'aime les frites !",
        "Les chats sont beau et joyeux, je les aimes !"]

#On transforme la liste de tweet en liste de liste de string (c'est a dire une liste de mots pour chaque tweet de la liste de tweet)          
listWordMsg=oTree.lemnise(msg)

#on transforme la liste de liste de mots en liste de coefficient (float) (c'est a dire un coeffcient par tweet, entre -1 et 1)
coefList = oTree.lemToCoef(listWordMsg)
print(coefList)
#On calcule le coefficient global pour la liste de tweet (on récupère un float en tre -1 et 1)
coef = oTree.calculateCoef(coefList)
print(coef)

#ci-dessous en commentaire la méthode pour mettre a jour le coef global dynamiquemet
"""
#on récupère la liste de coef des nouveau tweets
coefList2 = oTree.lemToCoef(oTree.lemnise(msg2))
#on la combine avec l'ancien coef pour calculer le nouveau coef (paramètre : ancien coef ; nb de tweet utilisés pour calculer l'ancien coef ; nouvelle liste de coefs.  On récupère le nouveau coef)
coef = oTree.actualizeCoef(coef, 6, coefList2)
print(coef)
"""

#Ci-dessous on affiche juste chaque row du dico
with open("dico", 'rb') as dictionary:
    depickler = pickle.Unpickler(dictionary)
    
    dictNP = depickler.load()

for row in dictNP.rowList:
    print("Mot : "+str(row.word)+"\n "+str(row.nbAppearPositive)+" - "+str(row.coefPositive)+"\n "+str(row.nbAppearNegative)+" - "+str(row.coefNegative))


