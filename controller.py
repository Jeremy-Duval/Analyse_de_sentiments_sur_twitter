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

def whatisthis(s):
    if isinstance(s, str):
        print "ordinary string"
    elif isinstance(s, unicode):
        print "unicode string"
    else:
        print "not a string"

def init_tweet(valeur):
    Listener = tweeter.listener()
    twitterStream = tweeter.Stream(tweeter.auth, Listener)
    tandances = twitterStream.listener.getTrends()
    print tandances[1]
    #teststring = unicode("😀😃😄😁😆😅😂🤣☺️😊🙂😇🙃😉😌😍😋🙋", 'utf-8')
    #teststring = teststring.encode('unicode_escape')
    teststring = "😀 😃 😄 😁 😆 😅 😂 🤣 ☺️ 😊 🙂 😇 🙃 😉 😌 😍 😋 🙋"
    print teststring
    tableau_positifs = teststring.split(" ")
    #tableau_positifs.pop(0)
    #tableau_positifs.append('U0001f62d')
    print tableau_positifs
    twitterStream.filter(track=[tandances[1]],languages = ["fr"], stall_warnings = True)
    liste = twitterStream.listener.retrieveList()#voici comment récupérer l'objet liste
    indices =[]
    for emojis in tableau_positifs:
        print emojis.lower()
        indices_traitement = [i for i, s in enumerate(liste) if emojis.lower() in s.encode('utf-8')]#chercher les emojis avec ça
        #whatisthis(s)
        #print indices_traitement
        indices = indices_traitement
        list(set(indices)|set(indices_traitement))
    print indices
    return indices
    #MachineLearning(liste)

  
def getTendance():
    Listener = tweeter.listener()
    twitterStream = tweeter.Stream(tweeter.auth, Listener)
    tandances = twitterStream.listener.getTrends()
    return tandances
    
    
def TfidVectorizer(messages):
    vectWord = TfidfVectorizer(analyzer='word',ngram_range=(1,2),max_df = 0.95,min_df=0.05)
    dtmWord = vectWord.fit_transform(messages)
    
    vectChar = TfidfVectorizer(analyzer='char',ngram_range=(3,5),max_df = 0.95,min_df=0.2)
    dtmChar = vectChar.fit_transform(messages)

    dtm = np.concatenate((dtmWord.toarray(), dtmChar.toarray()), axis=1)
    
    return np.array(dtm)

def MachineLearning(liste1,liste2):
    Xtransform = TfidVectorizer(liste1)
    Xtrain,Xtest,Ytrain,Ytest = train_test_split(Xtransform,liste2,random_state=3)
    
    clf = RandomForestClassifier(max_depth=2, random_state=0,n_estimators=1000,max_leaf_nodes=100)
    clf.fit(Xtrain,Ytrain)

    
    Ypredict = clf.predict(Xtest)
    accuracy_score(Ytest, Ypredict)

    
   