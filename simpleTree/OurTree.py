# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 16:04:28 2018

@author: Jérémy
"""

class OurTree:
    """
    Class to use our model of machine learning. 
    It's a simple model, similar to the tree in machine learning.
    It use a file with all word encounter, with their polarity (positiv/negativ ;
    they can appear 2 times in the file, one per polarity), the number of theirs
    apparition with this polarity and their importance coefficient (for this polarity).
    
    Require to download :  
    Spacy : sudo pip install spacy
    The french unit of Spacy : sudo python -m spacy download fr
    """

