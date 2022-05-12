import numpy as np
import pandas as pd
from sklearn import tree
input_file= 'PastHires.csv'

df= pd.read_csv(input_file)

print(df.head())