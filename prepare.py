#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, MinMaxScaler

import warnings
warnings.filterwarnings("ignore")

import acquire


# In[104]:


def cleaning(df):
    cols = df.columns[:4].tolist()
    df.drop(columns=cols, inplace=True)
    df['partner_dependent'] = df.partner.str.cat(df.dependents)
    df['streaming'] = df.streaming_tv.str.cat(df.streaming_movies)
    df['online_service'] = df.online_security.str.cat(df.online_backup)
    df['partner_dependent'] = df.partner_dependent.map({'NoNo': 0,
                                                        'YesNo': 1,
                                                        'NoYes': 1,
                                                        'YesYes': 1})
    df['streaming'] = df.streaming.map({'No internet serviceNo internet service':0, 
                                        'NoNo':0,
                                        'YesNo':1,
                                        'NoYes':1,
                                        'YesYes':1})
    df['online_service'] = df.online_service.map({'No internet serviceNo internet service':0,
                                                  'NoNo':0, 
                                                  'YesNo':1,
                                                  'NoYes':1,
                                                  'YesYes':1})
    df['multiple_lines'] = df.multiple_lines.map({'No phone service':0,
                                                  'No':1,
                                                  'Yes':1})
    df['internet_service_type'] = df.internet_service_type.map({'None':0,
                                                                'DSL':1,
                                                                'Fiber optic':1})
    df['payment_type'] = df.payment_type.map({'Electronic check':0, 
                                              'Mailed check':0,
                                              "Bank transfer (automatic)":1, 
                                              "Credit card (automatic)":1})
    df['contract_type'] = df.contract_type.map({'Month-to-month':0,
                                                'One year':1,
                                                'Two year':2})
    df['device_protection'] = df.device_protection.map({'No internet service':0,
                                                        'No':0, 
                                                        'Yes':1})
    df['tech_support'] = df.tech_support.map({'No internet service':0,
                                              'No':0, 
                                              'Yes':1})
    df['paperless_billing'] = df.paperless_billing.map({'No':0,
                                                        'Yes':1})
    df['churn'] = df.churn.map({'No':0,
                                'Yes':1})
    df['tenure_year'] = (df.tenure/12).round(1)
    gender_dummy = pd.get_dummies(df.gender, drop_first=True)
    df = pd.concat([df, gender_dummy], axis=1)
    df.drop(columns=['phone_service',
                     'online_security', 'online_backup',
                     'streaming_tv', 'streaming_movies',
                     'partner', 'dependents',
                     'gender'], inplace=True)
    return df


# In[105]:


def prep_telco_churn(df):
    df = cleaning(df)
    train_validate, test = train_test_split(df, test_size=0.2, 
                                            random_state=123, 
                                            stratify = df.churn)
    train, validate = train_test_split(train_validate, test_size=0.3, 
                                       random_state=123,
                                       stratify=train_validate.churn)
    return train, validate, test

