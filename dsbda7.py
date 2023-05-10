#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as pt
import numpy as np
import requests as r


# In[3]:


df=pd.read_csv("iris.csv")


# In[4]:


df


# In[10]:


df.columns=["Id","SepalLengthCm","SepalWidthCm","PetalLengthCm","PetalWidthCm","Species"]


# In[11]:


df


# In[12]:


df.info()


# In[13]:


df.isnull().sum()


# In[14]:


df.describe()


# In[15]:


df.drop_duplicates()


# In[17]:


pt.title("Frequency distribution of SepalLengthCm") 
pt.xlabel("X-axis")
pt.ylabel("Frequency")
df["SepalLengthCm"].hist(color="orange",bins=8)


# In[18]:


pt.title("Frequency distribution of SepalWidthCm") 
pt.xlabel("X-axis")
pt.ylabel("Frequency")
df["SepalWidthCm"].hist(color="orange",bins=8)


# In[19]:


pt.title("Frequency distribution of PetalLengthCm")
pt.xlabel("X-axis")
pt.ylabel("Frequency")
df["PetalLengthCm"].hist(color="orange",bins=8)


# In[21]:


pt.title("Frequency distribution of PetalWidthCm") 
pt.xlabel("X-axis")
pt.ylabel("Frequency")
df["PetalWidthCm"].hist(color="orange",bins=8)


# In[22]:


df["Species"].hist(color="orange")


# In[23]:


pt.boxplot(df["SepalLengthCm"])


# In[24]:


pt.boxplot(df["SepalWidthCm"])


# In[25]:


pt.boxplot(df["PetalLengthCm"])


# In[26]:


pt.boxplot(df["PetalWidthCm"])


# In[34]:


df[{"Id","SepalLengthCm","SepalWidthCm","PetalLengthCm","PetalWidthCm","Species"}].boxplot()
pt.title("Comparing all boxplots")


# In[ ]:




