# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 09:05:12 2021

@author: jnpi
"""
import os
import pandas as pd
os.chdir("C:\Jupiter\SZOT_trial\ce") 
cwd = os.path.abspath("C:\Jupiter\SZOT_trial\ce") 
files = os.listdir(cwd) 

df0=pd.DataFrame()
df1=pd.DataFrame()

for file in files:
    if file.endswith(".xlsx") and "CE86" in file :
        df0 = df0.append(pd.read_excel(file, skiprows=range(0,30)), ignore_index=False) 
        df1 = df1.append(pd.read_excel(file, sheet_name=1 , skiprows=range(0,9)), ignore_index=True) 
df0.head
df1.head
df0.to_excel('total.xlsx')
df1.to_excel('measurement.xlsx')

def data_appendix():
    os.chdir("C:\Jupiter\SZOT_trial\ce") 
    cwd = os.path.abspath("C:\Jupiter\SZOT_trial\ce") 
    files = os.listdir(cwd) 
    df0=pd.DataFrame()
    for file in files:
        if file.endswith(".xlsx") "and "CE86" in file" :
            df0 = df0.append(pd.read_excel(file, skiprows=range(0,30)), ignore_index=False) 
    df0.head
    df0.to_excel('total.xlsx')
    
