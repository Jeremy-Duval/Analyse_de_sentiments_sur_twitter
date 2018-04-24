#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 08:46:28 2018

@author: rukiny
"""
import sys
reload(sys)
import json
sys.setdefaultencoding("utf-8")
from flask import Flask, request, render_template, send_from_directory
import controller
from wtforms import Form, BooleanField, StringField, PasswordField, validators

class RechercheForm(Form):
    recherche = StringField('Recherche', [validators.Length(min=4, max=25)])

app = Flask(__name__)


#Lancer http://localhost:5000/ pour voir la page

@app.route('/getTendances')
def get_tendances():
    return json.dumps({'items': controller.getTendance()})

@app.route('/getTweets/')
def get_tweets():
    print 'HERE GET TWEETS'
    method1 = controller.getListeTweet(request.args.get('research'))
    method2 = controller.getListeTweetFonctionTree(request.args.get('research'))
    return json.dumps({'items': {'method1': method1, 'method2': method2}})


@app.route('/accueil')
def accueil_new():
    return render_template('accueil.html')


@app.route('/js/<path:path>')
def send_css(path):
    return send_from_directory('js', path)

@app.route('/dialogs/<path:path>')
def send_dialogs(path):
    return send_from_directory('templates/dialogs', path)


@app.route('/icons/<path:path>')
def send_icons(path):
    return send_from_directory('images/icons', path)

@app.route('/images/<path:path>')
def send_images(path):
    return send_from_directory('images', path)


@app.route('/css/<path:path>')
def send_js(path):
    return send_from_directory('css', path)


@app.route('/')
def accueil():
    tendance = controller.getTendance()
    mots = "Voici la page d'accueil !"
    form = RechercheForm(request.form)
    if request.method == 'GET':
        mots = controller.getListeTweet(form.recherche.data)
    return render_template('accueil.html', titre="Feel it !", mots=tendance, form=form, result=mots)

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



