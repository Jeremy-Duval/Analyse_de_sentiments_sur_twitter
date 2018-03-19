# -*- coding: utf-8 -*-
"""
Require to download :  
Spacy : sudo pip install spacy
The french unit of Spacy : sudo python -m spacy download fr

Created on Thu Mar  8 16:04:28 2018

@author: Jérémy
"""
import Tree
from DictionaryRow import DictionaryRow
from DictionaryNP import DictionaryNP
import pickle
import spacy
nlp = spacy.load('fr')


class OurTree:
    """
    Class to use our model of machine learning. 
    It's a simple model, similar to the tree in machine learning.
    It use a file with all word encounter, with their polarity (positiv/negativ ;
    they can appear 2 times in the file, one per polarity), the number of theirs
    apparition with this polarity and their importance coefficient (for this polarity).
    """
    
    def __init__(self):
        """
        Void constructor for our object
        """
        pass
    
    def lemnise(self, strList):
        """
        This method extract important word of string in param.
        Param : - strList : list of string : the function extract word of theirs strings
        Return : - list of list of string : for each string in param, we return 
                 a list of important word.
        """
        #TODO
        
    def lemToCoef(self, dStrList):
        """
        This method calculate the coefficient (positive or negative) for each
        list of list of word in param.
        Param : - dStrList : list of list of string : list of important word list.
        Return : - list of float : coefficients (<0 if negative, else positive)
        """
        #TODO
        
    def calculateCoef(self, coefList):
        """
        This method calculate the average of coefficients in the list.
        Param : coefList : list of float : list of coefficient 
                           (each of us correspond to a string treated before)
        Return : - float : global coefficient
        """
        #TODO
        
    def actualizeCoef(self, oldCoef, nbStr, dStrList):
        """
        This method calculate the new coefficient with the old.
        It permiss to use multi-threads or dynamic functionement working.
        Param : - oldCoef : float : the coefficient to actualize
                - nbStr : int : the number of list of string use to calculate oldCoef
                - dStrList : list of list of string : list of important word list.
                             serve to recalculate the new coefficient
        Return : - float : coefficient (<0 if negative, else positive)
        """
        #TODO
        
    def __actualizeDico__(self, word, coefficient):
        """
        This method actualize the dictionary file, with the new coefficient, 
        for each string treated. 
        Param : - word : string : the word to actualize (if it didn't appear in
                         the file, it will be add)
                - coefficient : float : the coefficient of the string where 
                                appear the word.
        Return : /
        """
        #TODO
        
    def __calcCoefWithTree__(self, wordList):
        """
        This method create a tree and calculate coeficients.
        Param : wordlist : list of string : list of sentence lemmas.
        Return : float : the coefficient of the list
        """
        root = Tree()
        
        with open("dico", 'rb') as dictionary:
            depickler = pickle.Unpickler(dictionary)
            dictNP = depickler.load()
            
        for row in dictNP.rowList:
            print(row.word)