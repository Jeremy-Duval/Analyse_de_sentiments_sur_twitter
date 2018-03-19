# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 16:46:25 2018

@author: jeremy
"""

class DictionaryRow:
    def __init__(self, word, coefPositive, coefNegative):
        self.word = word
        self.nbAppearPositive = 1
        self.coefPositive = coefPositive
        self.nbAppearNegative = 1
        self.coefNegative = coefNegative