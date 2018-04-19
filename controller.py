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





# =============================================================================
# def whatisthis(s):
#     if isinstance(s, str):
#         print "ordinary string"
#     elif isinstance(s, unicode):
#         print "unicode string"
#     else:
#         print "not a string"
# =============================================================================

def init_tweet():
    Listener = tweeter.listener()
    twitterStream = tweeter.Stream(tweeter.auth, Listener)
    return twitterStream
    #MachineLearning(liste)

def getListeTweet(valeur):
    twitterStream = init_tweet()
    tendance = twitterStream.listener.getTrends()

    #teststring = unicode("😀😃😄😁😆😅😂🤣☺️😊🙂😇🙃😉😌😍😋🙋", 'utf-8')
    #teststring = teststring.encode('unicode_escape')
   
    twitterStream.filter(track=[tendance[0]],languages = ["fr"], stall_warnings = True)
    liste = twitterStream.listener.retrieveList()#voici comment récupérer l'objet liste
    
    listeSentiment = getListeSentiment(liste)
    MachineLearn = MachineLearning(liste,listeSentiment)
    return MachineLearn
    

def getListeSentiment(liste):
    stringpos = "😀 😃 😄 😁 😆 😅 😂 🤣 ☺️ 😊 🙂 😇 🙃 😉 😌 😍 😋 🙋 :D ^^ 👍 👐 🤗 ✌️ 😎 🤩 😸 😹 😺 😻 :) ❤️ 🧡 💛 💚 💙 💜 🖤"
    tableau_positifs = stringpos.split(" ")
    indicesp = []
    liste_final= range(len(liste))
    for emojis in tableau_positifs:
        #print emojis.lower()
        indices_traitementp = [i for i, s in enumerate(liste) if emojis.lower() in s.encode('utf-8').lower()]#chercher les emojis avec ça
        #print indices_traitement
        #print indices_traitement
        indicesp = indicesp + indices_traitementp

    liste_positifs = list(set(indicesp))
    
    for i in liste_positifs:
        liste_final[i] = "POSITIF"
    
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
    print liste_negatifs
    
    for i in liste_negatifs:
        liste_final[i] = "NEGATIF"
        
    for i in liste_final:
        if i != "NEGATIF" and i != "POSITIF":
            liste_final[i] = "NEUTRE"
    
    return liste_final
  
def getTendance():
    twitterStream = init_tweet()
    tendance = twitterStream.listener.getTrends()
    return tendance

def MachineLearning(liste1,liste2):
    Xtransform = TfidVectorizer(liste1)
    Xtrain,Xtest,Ytrain,Ytest = train_test_split(Xtransform,liste2,random_state=3)
    
    clf = RandomForestClassifier(max_depth=2, random_state=0,n_estimators=1000,max_leaf_nodes=100)
    clf.fit(Xtrain,Ytrain)
    
    Ypredict = clf.predict(Xtest)
    #Teste le niveau de fiabilité !
    #accuracy_score(Ytest, Ypredict)
    
    ListeSentiment =  np.concatenate((Ytrain, Ypredict), axis=0)

    cptPositif = 0
    cptNegatif = 0
    cptNeutre = 0
    for i in ListeSentiment:
        if i == "POSITIF":
            cptPositif = cptPositif+1
        if i == "NEGATIF":
            cptNegatif = cptNegatif+1
        if i == "NEUTRE":
            cptNeutre = cptNeutre+1
    if cptNeutre > cptPositif and cptNeutre > cptNegatif:
        return "NEUTRE à "+str((float(cptNeutre)/len(ListeSentiment))*100)+"%"
    if cptPositif > cptNegatif:
        return "POSITIF à "+str((float(cptPositif)/len(ListeSentiment))*100)+"%"
    if cptNegatif > cptPositif:
        return "NEGATIF à "+str(float(cptNegatif/len(ListeSentiment))*100)+"%"
            

def TfidVectorizer(messages):
    vectWord = TfidfVectorizer(analyzer='word',ngram_range=(1,2),max_df = 0.95,min_df=0.05)
    dtmWord = vectWord.fit_transform(messages)
    
    vectChar = TfidfVectorizer(analyzer='char',ngram_range=(3,5),max_df = 0.95,min_df=0.2)
    dtmChar = vectChar.fit_transform(messages)

    dtm = np.concatenate((dtmWord.toarray(), dtmChar.toarray()), axis=1)
    
    return np.array(dtm)
