#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 20:23:58 2018

@author: rukiny
"""

import tweeter
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import FeatureUnion
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
#OurTree model
import pickle
from OurTree import *
from DictionaryRow import DictionaryRow
from DictionaryNP import DictionaryNP




# =============================================================================
# def whatisthis(s):
#     if isinstance(s, str):
#         print "ordinary string"
#     elif isinstance(s, unicode):
#         print "unicode string"
#     else:
#         print "not a string"
# =============================================================================

#Appel de l'api tweepy
def init_tweet():
    Listener = tweeter.listener()
    twitterStream = tweeter.Stream(tweeter.auth, Listener)
    return twitterStream
    
def getListeTweet(valeur):
    twitterStream = init_tweet()
    twitterStream.filter(track=[str(valeur).encode('utf8')], languages=["fr"], stall_warnings=True)
    liste = twitterStream.listener.retrieveList()#voici comment récupérer l'objet liste
    return liste


def MachineLearning(liste):
    stringpos = "😀 😃 😄 😁 😆 😅 😂 🤣 ☺️ 😊 🙂 😇 🙃 😉 😌 😍 😋 🙋 :D ^^ 👍 👐 🤗 ✌️ 😎 🤩 😸 😹 😺 😻 :) ❤️ 🧡 💛 💚 💙 💜 🖤"
    tableau_positifs = stringpos.split(" ")
    indicesp = []
    liste_final=[]
    listeTriEmoticone = []
    listeSentiment=[]
    for emojis in tableau_positifs:
        #print emojis.lower()
        indices_traitementp = [i for i, s in enumerate(liste) if emojis.lower() in s.encode('utf-8').lower()]#chercher les emojis avec ça
        #print indices_traitement
        #print indices_traitement
        indicesp = indicesp + indices_traitementp
    liste_positifs = list(set(indicesp))

    for i in liste_positifs:
        listeTriEmoticone.append(liste[i])
        listeSentiment.append(1)
        liste.remove(liste[i])
    

    stringneg = "😒 😞 😔 😟 😕 🙁 ☹️ 😖 😣 😫 😩 😢 😭 😤 😠 😡 🤬 🤯 😨 😱 😰 😥 😓 🤒 🤕 👎 😾 :("
    tableau_negatifs = stringneg.split(" ")
    indicesn =[]
    for emojis in tableau_negatifs:
        #print emojis.lower()
        indices_traitement = [i for i, s in enumerate(liste) if emojis.lower() in s.encode('utf-8').lower()]#chercher les emojis avec ça
        #print indices_traitement
        #print indices_traitement
        indicesn = indicesn + indices_traitement
    liste_negatifs = list(set(indicesn))

    for i in liste_negatifs:
        listeTriEmoticone.append(liste[i])
        listeSentiment.append(-1)
        liste.remove(liste[i])
    
    for i in liste:
        listeSentiment.append(0)
    
    if(listeTriEmoticone != []):
        liste_final = listeTriEmoticone+liste  
        #return str(len(liste_final))+str(len(listeTriEmoticone))+str(len(liste))
        #Machine Learning
        Xtransform = TfidVectorizer(liste_final)
        Xtrain,Xtest,Ytrain,Ytest = train_test_split(Xtransform,listeSentiment,train_size=len(listeTriEmoticone),random_state=len(listeTriEmoticone))
    
        clf = RandomForestClassifier(max_depth=2, random_state=0,n_estimators=1000,max_leaf_nodes=100)
        clf.fit(Xtrain,Ytrain)
    
        Ypredict = clf.predict(Xtest)
        sentiment = np.concatenate((Ytrain, Ypredict), axis=0)
    
        #Teste le niveau de fiabilité !
        #accuracy_score(Ytest, Ypredict)
        cptPositif = 0
        cptNegatif = 0
        for i in sentiment:
            if i > 0:
                cptPositif = cptPositif+1
            if i < 0:
                cptNegatif = cptNegatif+1
        if cptPositif == cptNegatif:
            return "NEUTRE"
        if cptPositif > cptNegatif:
            return "POSITIF à "+str((float(cptPositif)/len(liste_final))*100)+"%"
        if cptNegatif > cptPositif:
            return "NEGATIF à "+str((float(cptNegatif)/len(liste_final))*100)+"%"

    else:
        return "Pas d'émoticones trouvés, il faut augmenter le nombre de tweet..."


def getTendance():
    twitterStream = init_tweet()
    tendance = twitterStream.listener.getTrends()
    return tendance



def TfidVectorizer(messages):
    vectWord = TfidfVectorizer(analyzer='word',ngram_range=(1,2),max_df = 0.95,min_df=0.05)
    dtmWord = vectWord.fit_transform(messages)

    vectChar = TfidfVectorizer(analyzer='char',ngram_range=(3,5),max_df = 0.95,min_df=0.2)
    dtmChar = vectChar.fit_transform(messages)

    dtm = np.concatenate((dtmWord.toarray(), dtmChar.toarray()), axis=1)

    return np.array(dtm)

    
def OurMachineLearning(tweetList):
    """
    This method call the module our tree and return a coefficient between -1 and 1.
    Param : - tweetList : list of string : list of tweet
    Return : - string : resultat
    """  
    #Our tree model creation 
    oTree = OurTree()
    #we transform the list of tweet in list of list of string (a list of word for each tweet)
    listWordMsg=oTree.lemnise(tweetList)
   
    #print("******************************")
    #print(listWordMsg)
   
    #we transform the list of list of word in list of coefficient (a coef for each tweet)
    coefList = oTree.lemToCoef(listWordMsg)    
    #we calculate the global coef (for the list of tweet)
    coef = oTree.calculateCoef(coefList)
    
    if coef>0:
        return "POSITIF à "+str(coef*100)+"%"
    elif coef<0:
        return "NEGATIF à "+str(-coef*100)+"%"
    else :
        return "Le dictionnaire n'a pas permis de déterminer un résultat"                                                                           
                                                                                                                        