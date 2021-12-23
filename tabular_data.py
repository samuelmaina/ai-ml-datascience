import matplotlib

import numpy as np
import pandas as pd

#pd loads the dat into dataframe
df=pd.read_csv('PastHires.csv')

#read the first few values from a dataflame
print(df.head()) #the default being 5
print(df.head(10)) # one can specify the vales that they need to view.

print(df.tail()) #prints the last five records 
print(df.tail(10)) #prints the last specific records

