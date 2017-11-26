
# coding: utf-8

# In[4]:


import pandas as pd


# In[35]:


url = "http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&render=download"
Nasdaq = pd.read_csv(url)
Nasdaq


# In[28]:


url = "http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NYSE&render=download"
NYSE = pd.read_csv(url)
NYSE


# In[29]:


URL="http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=AMEX&render=download"
AMEX = pd.read_csv(url)
AMEX
