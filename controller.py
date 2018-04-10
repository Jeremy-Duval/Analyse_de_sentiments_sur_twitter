#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 20:23:58 2018

@author: rukiny
"""

import tweeter

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
    twitterStream.filter(track=[u'\U0001f600'],languages = ["fr"], stall_warnings = True)
    liste = twitterStream.listener.retrieveList()#voici comment récupérer l'objet liste
    indices =[]
    for emojis in tableau_positifs:
        print emojis.lower()
        indices_traitement = [i for i, s in enumerate(liste) if emojis.lower() in s.encode('utf-8')]#chercher les emojis avec ça
        #whatisthis(s)
        print indices_traitement
        indices = indices_traitement#list(set(indices)|set(indices_traitement))
    print indices
    