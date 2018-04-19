#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 08:46:28 2018

@author: rukiny
"""
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from flask import Flask, request, render_template
import controller

app = Flask(__name__)


#Lancer http://localhost:5000/ pour voir la page

@app.route('/')
def accueil():
    tendance = controller.getTendance()

    return render_template('accueil.html', titre="Feel it !", mots=tendance,result="Voici la page d'accueil !")

@app.route('/tweet/<mot>')
@app.route('/tweet/#<mot>')
def recupTweet(mot):
    tendance = controller.getTendance()
    mots = controller.getListeTweet(" ")
    
    return render_template('accueil.html', titre="Feel it !", mots=tendance,result=mots)

@app.route('/Recherche')
def test():
    indices = controller.init_tweet(" ")

if __name__ == '__main__':

    app.run(debug=True)


