#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import os
import env


# In[2]:


def get_connection(db, user=env.user, host=env.host, password=env.password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'


# In[3]:


def get_telco_churn_data():
    filename = 'telco_churn.csv'
    
    if os.path.isfile(filename):
        return pd.read_csv(filename, index_col=0)
    else: 
        df = pd.read_sql("""select * 
                        from customers join contract_types using(contract_type_id) 
                        join internet_service_types using(internet_service_type_id) 
                        join payment_types using(payment_type_id)""", get_connection('telco_churn'))
        df.to_csv(filename)
        return df

