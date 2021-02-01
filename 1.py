# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 13:52:07 2021

@author: jnpi
"""

import pandas as pd
import os
 
df0=pd.DataFrame()
cwd=r"C:\Jupiter\JPH\Jupiter jig data"
result=os.listdir(cwd)
print(result)
for dir_ in result:
    files=os.listdir(os.path.join(cwd,dir_))
    for files_ in files:
         if files_.endswith(".xlsx") and "PX75" in files_ :
             print(os.path.join(dir_,files_))
             "df0=df0.append(pd.read_excel(os.path.join(cwd,dir_,files_), skiprows=range(0,30)), ignore_index=False)" 
             df0=df0.append(pd.read_excel(os.path.join(cwd,dir_,files_), sheet_name=1 , skiprows=range(0,9)), ignore_index=False) 
df0.head
df0.to_excel('PX75_1.xlsx')



"""
for direc in result[][]
files = os.listdir(cwd) 

df0=pd.DataFrame()
df1=pd.DataFrame()

for file in files:
    if file.endswith(".xlsx") and "CE86" in file :
        df0 = df0.appwend(pd.read_excel(file, skiprows=range(0,30)), ignore_index=False) 
        df1 = df1.append(pd.read_excel(file, sheet_name=1 , skiprows=range(0,9)), ignore_index=True) 
df0.head
df1.head
df0.to_excel('total.xlsx')
df1.to_excel('measurement.xlsx')
"""