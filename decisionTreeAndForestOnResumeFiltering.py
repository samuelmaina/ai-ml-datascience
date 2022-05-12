import numpy as np
import pandas as pd
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt

input_file= 'PastHires.csv'

df= pd.read_csv(input_file)

print(df.head())

#to convert Yes No values to numerical values
yesNo= {"Y" :1, "N":0}

df["Hired"]= df["Hired"].map(yesNo)
df["Employed?"]= df["Employed?"].map(yesNo)
df["Top-tier school"]= df["Top-tier school"].map(yesNo)
df["Interned"]= df["Interned"].map(yesNo)



#the same for the levels of education.
education={"BS":0,  "MS":1, "PhD": 2}
df["Level of Education"]= df["Level of Education"].map(education)

print(df.head())


#extract the features from the data that will be used for prediction.
features= list(df.columns[:6])
print(features)




y=df["Hired"]
x= df[features]
classifier=tree.DecisionTreeClassifier()
classifier= classifier.fit(x,y)
#TODOs check on how to generate the decision tree image.
print(classifier)


#to prevent overfiting Random forest are used to make the decision.
#The forest consists of many trees in which each acts on random sample of the 
#data . On the overall decision each tree makes a vote  which will contribute
#to overall decisions








