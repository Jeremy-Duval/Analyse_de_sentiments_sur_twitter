# -*- coding: utf-8 -*-
"""
Require to download :  
Spacy : sudo pip install spacy
The french unit of Spacy : sudo python -m spacy download fr

Created on Thu Mar  8 16:04:28 2018

@author: Jérémy
"""
from Tree import Tree
from DictionaryRow import DictionaryRow
from DictionaryNP import DictionaryNP
import pickle
import spacy
import unicodedata

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
        @author: Jenny,modified by Jérémy
        """
        listListWord = list()
        
        for sentence in strList :
            sentUni1 = unicode(sentence,'utf-8')
            sentUni2 = unicodedata.normalize('NFD', sentUni1).encode('ascii', 'ignore')  
            doc = nlp(sentUni2.decode('unicode-escape'))
            listListWord.append(self.__lemma__(doc))
        return listListWord
    
    def __lemma__(self, doc):
        """
        This method return the list of important words for the sentence.
        Param : - doc : spacy unicode document : the sentence from where we extract words
        Return : - list of string : list of words extract from the sentence
        @author: Jenny,modified by Jérémy
        """
        listWord = list()
        for token in doc:
            if token.pos_ == 'ADJ' or token.pos_ == 'SYM' or token.pos_ == 'ADV' or token.pos_ == 'VERB':
                listWord.append(token.lemma_)
        return listWord

        
    def lemToCoef(self, dStrList):
        """
        This method calculate the coefficient (positive or negative) for each
        list of list of word in param.
        Param : - dStrList : list of list of string : list of important word list.
        Return : - list of float : coefficients (<0 if negative, else positive)
        """
        #TODO
            #-call Tree
            #-actualize dico (coef et mots potentiels)
        
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
        coef = 0.0
        div = 0.0
        
        with open("dico", 'rb') as dictionary:
            depickler = pickle.Unpickler(dictionary)
            dictNP = depickler.load()
        
        self.__constructTree__(wordList, root, dictNP)
        
        if (root.left!=None) or (root.right!=None) :
           listLeaf = list()
           self.__treeLeafsCoef__(root, listLeaf)
           for leaf in listLeaf:
               print("Leaf :")
               print(leaf)
               coef = coef+leaf
               div = div+abs(leaf)
           coef = coef / div
        print("coef :")
        print(coef)
        
        return coef
                    
    def __constructTree__(self, wordList, root, dictNP):
        """
        This method create a tree and calculate coeficients recursively.
        Param : wordlist : list of string : list of sentence lemmas.
                root : Tree : the root of the tree.
                dico : DictionaryNP : a dictionary of word with theirs +/- correspondance
        """
        ##listCandidate = list()  
        ##listReturned = list()
        ##wordIsCandidate=False #var to know if the word is already in dictionary and if we need to add it  
        wordFind=False
        passInPos=False
        passInNeg=False
        if root.data != None :
            coef=root.data
        else :
            coef = 0
        if wordList==[] :
            pass
        else :            
            word = wordList.pop()
            print("*******")            
            print(word)
            ##print("_______") 
            for row in dictNP.rowList:
                ##print(row.word)
                if(row.word==word):
                    wordFind=True
                    #a coef = coefRoot+coefWordActu ; (-CoefWordActu if negative)
                    if(row.coefPositive!=None):
                        passInPos=True
                        posTree = Tree()
                        posTree.data=row.coefPositive+coef
                        root.left = posTree
                        wordList2 = list(wordList) #if the word is + and - we need to clone the list to use it in - branch
                        print("..........")
                        print(str(posTree.data)+" | "+str(posTree.left)+" | "+str(posTree.right))
                        print("..........")
                        ##listReturned = self.__constructTree__(wordList, posTree, dictNP)
                        self.__constructTree__(wordList, posTree, dictNP)
                    if(row.coefNegative!=None):
                        passInNeg=True
                        negTree = Tree()
                        negTree.data=-row.coefNegative+coef
                        print("..........")
                        print(str(negTree.data)+" | "+str(negTree.left)+" | "+str(negTree.right))
                        print("..........")
                        root.right = negTree
                        ##listReturned = self.__constructTree__(wordList, negTree, dictNP)
                        if(passInPos):
                            self.__constructTree__(wordList2, negTree, dictNP)    
                        else :    
                            self.__constructTree__(wordList, negTree, dictNP)
                    if(passInPos!=True)and(passInNeg!=True):
                        ##listCandidate.append(word)
                        ##listReturned = self.__constructTree__(wordList, root, dictNP)
                        print("..........")
                        print("..........")
                        self.__constructTree__(wordList, root, dictNP)
            if (wordFind!=True) :
                self.__constructTree__(wordList, root, dictNP)
            ##print("Retour mots candidats :")                        
            ##print(listReturned)
            ##if(listReturned!=[]):
                ##listCandidate.extend(listReturned)
                                
        ##return listCandidate
                                
    def __treeLeafsCoef__(self, root, listLeafs) :
        """
        This method return a list with coefficients in tree's leafs.
        Param : root : Tree : the root of the tree.
                listLeafs : list of float : list wich will contains 
                                            coefficients in tree's leafs.
        """
        if (root.left==None) and (root.right==None) :
            listLeafs.append(root.data)
        else:
            if(root.left!=None):
                self.__treeLeafsCoef__(root.left, listLeafs)
                
            if(root.right!=None):
                self.__treeLeafsCoef__(root.right, listLeafs)