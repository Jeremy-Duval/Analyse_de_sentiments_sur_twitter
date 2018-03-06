#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 08:46:28 2018

@author: rukiny
"""

from Tkinter import *
import tweeter

        
fenetre = Tk()

label = Label(fenetre, text="Feel It")
label.pack()

fenetre['bg']='white'

Frame1 = Frame(fenetre, borderwidth=2, relief=GROOVE)
Frame1.pack(side=LEFT, padx=30, pady=30)

Label(Frame1, text="Tweets recherchés").pack(padx=10, pady=10)

value = StringVar() 
entree = Entry(Frame1, textvariable=value, width=30)
entree.pack()

def saisie():
    valeur = entree.get()
    Listener = tweeter.listener()
    twitterStream = tweeter.Stream(tweeter.auth, Listener)
    #le contenu de la recherche se met ici dans track
    twitterStream.filter(track=[valeur],languages = ["fr"], stall_warnings = True)
    
bouton = Button(Frame1, text="Valider",command = saisie)
bouton.pack()

fenetre.mainloop()
