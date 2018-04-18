#!/usr/bin/env python2
# -*- coding: utf-8 -*-

 
from Tkinter import *
import controller
   
fenetre = Tk()
 
label = Label(fenetre, text="Feel It")
label.pack()
 
fenetre['bg']='white'
 
Frame1 = Frame(fenetre, borderwidth=2, relief=GROOVE)
Frame1.pack(side=TOP, padx=5, pady=5)
 
Label(Frame1, text="Tweets recherchés").pack(padx=10, pady=10)
 
value = StringVar() 
entree = Entry(Frame1, textvariable=value, width=30)
entree.pack()
 
liste = Listbox(fenetre)
tendance = controller.getTendance()
i=1
for x in tendance:
    liste.insert(1,x)
    i=i+1
 
 
liste.pack()
 
def saisie():
    valeur = entree.get()
    controller.init_tweet(valeur)