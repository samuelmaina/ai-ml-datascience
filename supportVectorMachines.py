from math import radians
from numpy import random
import numpy as np



#the same function as the one for creating kmeans clustered data but
#since there will be supervised learning add the cluster number to the data.
def createClusteredData(N, k):
    pointsPerCluster= float(N)/k 
    X=[]
    Y=[]
    for i in range(k):
        incomeCentroid= random.uniform(20000.0,200000.0)
        ageCentroid= random.uniform(20.0, 70.0);
        for j in range(int(pointsPerCluster)):
            X.append({random.normal(incomeCentroid, 10000.0), random.normal(ageCentroid,2.0)})
            Y.append(i)
    X= np.array(X)
    Y= np.array(Y)