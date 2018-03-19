# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 16:46:25 2018

@author: jeremy
"""

class DictionaryRow:
    def __init__(self):
        self.word = None
        self.nbAppearance = None
        self.coefPositive = None
        self.coefNegative = None
        
    def __init__(self, word, nbAppearance, coefPositive, coefNegative):
        self.word = word
        self.nbAppearance = nbAppearance
        self.coefPositive = coefPositive
        self.coefNegative = coefNegative