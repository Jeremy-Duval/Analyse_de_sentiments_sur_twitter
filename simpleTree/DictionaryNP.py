# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 10:53:00 2018

@author: jeremy
"""

class DictionaryNP(list):
    def __init__(self):
        self.rowList=[]
        
    def append(self, obj):
        self.rowList.append(obj)
        