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
from wtforms import Form, BooleanField, StringField, PasswordField, validators

class RechercheForm(Form):
    recherche = StringField('Recherche', [validators.Length(min=4, max=25)])

app = Flask(__name__)


#Lancer http://localhost:5000/ pour voir la page

@app.route('/')
def accueil():
    tendance = controller.getTendance()
    mots = "Voici la page d'accueil !"
    form = RechercheForm(request.form)
    if request.method == 'GET':      
        mots = controller.getListeTweet(form.recherche.data)
        
    return render_template('accueil.html', titre="Feel it !", mots=tendance,form=form,result=mots)

@app.route('/<mot>')
@app.route('/#<mot>')
def recupTweet(mot):
    tendance = controller.getTendance()
    mots = controller.getListeTweet(mot)
    form = RechercheForm(request.form)
    if request.method == 'GET':      
        mots = controller.getListeTweet(form.recherche.data)
        
    return render_template('accueil.html', titre="Feel it !", mots=tendance,form=form,result=mots)


if __name__ == '__main__':

    app.run(debug=True)



