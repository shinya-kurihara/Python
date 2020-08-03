#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[7]:


pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 5)


# In[8]:


df=pd.read_csv('data.csv', encoding='shift-jis')
df


# In[9]:


df.index = df.index +1


# In[10]:


df


# In[11]:


df.index


# In[12]:


df[0:3]


# In[15]:


df[9:14]


# In[16]:


df['人口（総数）'][:5]


# In[17]:


df[['人口（総数）']][:5]


# In[18]:


df[['都道府県名','人口（総数）']][:5]


# In[19]:


df['西暦（年）'] == 2015


# In[21]:


df[df['西暦（年）'] == 2015]


# In[22]:


df[df['都道府県名'] == '東京都']


# In[25]:


df['西暦（年）'] % 10 == 0


# In[26]:


df[df['西暦（年）'] % 10 == 0]


# In[28]:


df[~(df['西暦（年）'] % 10 == 0)]


# In[29]:


df[df['西暦（年）'] % 10 != 0]


# In[31]:


df[(df['西暦（年）'] == 2015) & (df['都道府県名'] == '東京都')]


# In[32]:


df[(df['西暦（年）']==2010) | (df['西暦（年）']==2015)]


# In[33]:


df = df.rename(columns={'西暦（年）': 'year'})


# In[34]:


df


# In[35]:


df.query('year == 2010')


# In[36]:


df.query('year > 2010')


# In[41]:


df.query('都道府県名 == "東京都"')


# In[42]:


df.query('year == 2010 or year == 2015')


# In[43]:


df.query('都道府県名 == "東京都" and year == 2015')


# In[45]:


df['year'].isin([2010])


# In[46]:


df[df['year'].isin([2010])]


# In[47]:


df[df['year'].isin([2010,2015])]


# In[48]:


df['都道府県名'].str.contains('山')


# In[49]:


df[df['都道府県名'].str.contains('山')]


# In[52]:


df[df['都道府県名'].str.endswith('道')]


# In[53]:


df[df['year']== df['year'].max()]


# In[55]:


df.loc[893,['人口（男）','人口（女）']]


# In[56]:


pd.set_option('display.max_rows', None)


# In[57]:


df


# In[58]:


df[150:156]


# In[65]:


df[(df['year'] == 2015) & (df['人口（総数）'] >=  5000000)]


# In[66]:


df.query('year == 2015 and 人口（総数） >= 5000000')


# In[67]:


df = df.rename(columns={'人口（総数）': 'population'})


# In[68]:


df.head(5)


# In[70]:


df.query('population >= 10000000 or population <= 500000')


# In[71]:


df[df['都道府県名'].isin(['沖縄県','北海道'])]


# In[76]:


df[df['都道府県名'].str.contains('川')]


# In[77]:


df[df['都道府県名'].str.startswith('北')]


# In[79]:


df[df['都道府県名'].str.endswith('府')]


# In[ ]:




