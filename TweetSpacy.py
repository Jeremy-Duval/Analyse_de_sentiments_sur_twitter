
# coding: utf-8

# In[3]:


import spacy
nlp = spacy.load('fr')


# In[22]:


#print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
#                  token.shape_, token.is_alpha, token.is_stop)
def Lemma(doc):
    liste = list()
    for token in doc:
        if token.pos_ == 'ADJ' or token.pos_ == 'SYM' or token.pos_ == 'ADV':
            liste.append(token.lemma_)
    return liste


# In[23]:


message = ["J\'ai faim",
          "La vie est belle",
          "J\'aime les chats",
          "Je pense que ça va"]
for m in message :  
    doc = nlp(m.decode('unicode-escape'))
    liste = Lemma(doc)
    for i in liste:
        print(i)


# In[19]:




