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
    #le contenu de la recherche se met ici dans track
    twitterStream.filter(track=[valeur],languages = ["fr"], stall_warnings = True)
    liste = twitterStream.listener.retrieveList()#voici comment récupérer l'objet liste