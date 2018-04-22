
# coding: utf-8

# In[2]:


from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

messages = ["Bonjour, les amis !",
           "Amour amour amour",
           "Tristesse tristesse tristesse",
           "La vie est belle"]


vect = CountVectorizer()
vect.fit(messages)


vect.get_feature_names()

dtm = vect.transform(messages)

pd.DataFrame(dtm.toarray(), columns=vect.get_feature_names())



# In[17]:


from sklearn.feature_extraction.text import TfidfVectorizer

def createDTM(messages):
    vect = TfidfVectorizer()
    dtm = vect.fit_transform(messages) # create DTM
    for test in vect.get_feature_names():
        print(test)
    # create pandas dataframe of DTM
    return pd.DataFrame(dtm.toarray(), columns=vect.get_feature_names()) 

messages = ["Bonjour, les amis !",
           "Amour amour amour",
           "Tristesse tristesse tristesse",
           "La vie est belle",
           "La nuit est longue",
           "Pourquoi la vie?"]

createDTM(messages)

