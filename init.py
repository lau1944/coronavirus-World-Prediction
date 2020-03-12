import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("data_reform.csv") 

#group = data.groupby('Country/Region').sum(
'''
data = data.drop(data.columns[[0,1,2,3]], axis=1)
for col in data.columns:
    data.at['Total',col] = data[col].sum()
   
data.to_csv("data_reform.csv", sep='\t', encoding='utf-8')
'''
timeline = []
count = []
for col in data.columns:
    timeline.append(col)
    count.append(data.at[0,col])

    print(int(col.replace('2020-','').replace('-','')))
    #print(data.at[0,col])

