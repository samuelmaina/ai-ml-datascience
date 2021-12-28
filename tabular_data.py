import matplotlib as plt

import numpy as np
import pandas as pd

#pd loads the dat into dataframe
df=pd.read_csv('PastHires.csv')

#read the first few values from a dataflame
print(df.head()) #the default being 5
print(df.head(10)) # one can specify the vales that they need to view.

print(df.tail()) #prints the last five records 
print(df.tail(10)) #prints the last specific records


print(df.shape) #used to get the number rows and columns
print(df.size) #used to get the total number of cells in the data
 
 
print(df.columns) #used to get the name of columns in the data frame.

print(df['Hired']) 
                    #used to extract data from the given column and load it 
                    #load it to a new df. Mostly only some few columns are need for
                    #data manipulation. They a
                   

print(df["Hired"][:5]) #used to extract the first five rows from
                  #the selected columns

print(df["Hired"][5]) #used to extract an exact value

degree_counts= df['Level of Education'].value_counts()
#to print the number of unique data values in a df
print(degree_counts)

degree_counts.plot(kind='bar')


