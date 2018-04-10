#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 20:23:58 2018

@author: rukiny
"""

import tweeter

def init_tweet(valeur):
    Listener = tweeter.listener()
    twitterStream = tweeter.Stream(tweeter.auth, Listener)
    tandances = twitterStream.listener.getTrends()
    print tandances[1]
    twitterStream.filter(track=[tandances[0]],languages = ["fr"], stall_warnings = True)
    liste = twitterStream.listener.retrieveList()#voici comment récupérer l'objet liste
    print liste
    indices = [i for i, s in enumerate(liste) if 'je' in s.lower()]#chercher les emojis avec ça
    print indices