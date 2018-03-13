
# coding: utf-8

# In[6]:


import spacy
nlp = spacy.load('fr')


# In[17]:


doc = nlp(u'J\'aime bien les chat anxieux, tristes, excités, joyeux, heureux')


# In[38]:


#print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
#                  token.shape_, token.is_alpha, token.is_stop)
def Lemma(doc):
    liste = list()
    for token in doc:
        if token.pos_ == 'ADJ' or token.pos_ == 'SYM' or token.pos_ == 'ADV':
            liste.append(token.lemma_)
            
    return liste


# In[39]:


print(Lemma(doc))

