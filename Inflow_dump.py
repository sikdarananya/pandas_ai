#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install llama-index')


# In[6]:


pip install llama-index-experimental


# In[21]:


pip install pandasai


# In[7]:


import pandas as pd
from IPython.display import Markdown, display

from llama_index.experimental.query_engine import PandasQueryEngine


# In[8]:


df = pd.read_excel('Wyndham_Managed_services_6M_Inflow.xlsx', '6M_Inflow')
df.head()


# In[11]:


import llama_index


# In[12]:


pip install openai


# In[14]:


pip install llama-index-llms-openai


# In[15]:


pip install llama-index-llms-azure-openai


# In[18]:


import openai
import os
from llama_index.llms.openai import OpenAI
from llama_index.llms.azure_openai import AzureOpenAI

import logging

import sys
 
logging.basicConfig(

    stream=sys.stdout, level=logging.INFO

)  # logging.DEBUG for more verbose output

logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))


# In[19]:


api_key ="3289261e6cc84fa8aef58d38e2264fa9"

openai.api_key = api_key

openai.api_base = "https://openai-demo-mb-001.openai.azure.com/"

openai.api_type = 'azure'

openai.api_version = '2023-05-15'

deployment_name = 'openaidemomb001'

deployment_name_embeddings = 'openaidemomb002'
 
os.environ["OPENAI_API_TYPE"] = openai.api_type

os.environ["OPENAI_API_VERSION"] = openai.api_version

os.environ["OPENAI_API_BASE"] = openai.api_base

os.environ["OPENAI_API_KEY"] = "3289261e6cc84fa8aef58d38e2264fa9"
llm = AzureOpenAI(

        deployment_name=deployment_name,

        model_name=deployment_name,

        cache=False,

        api_key=api_key,

        azure_endpoint=openai.api_base,

        temperature=0.1)


# In[24]:


os.environ["PANDASAI_API_KEY"] = "$2a$10$Ak52bQ/Dg89kTLbwNCMPtul3UsqBtFGEanEUklFk0WzdDr8joYICm"


# In[25]:


from pandasai import Agent


# In[26]:


agent = Agent(df)


# In[29]:


agent.chat('What is the category of INC2390627?')


# In[ ]:




