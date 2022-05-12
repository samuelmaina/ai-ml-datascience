from numpy import random

import numpy as np
import matplotlib.pyplot  as plt
from sklearn.preprocessing import scale
from sklearn.cluster import KMeans



#function to generated pure centroid. It is useful 
#in making sure that the model is working as intended.
def createClusteredData(N, k):
    random.seed(10)
    pointPerCluster= float(N)/k;
    X=[]
    for i in range(k):
        incomeCentroid= random.uniform(20000.0, 200000.0)
        ageCentroid= random.uniform(20.0, 70.0)
        for j in range(int(pointPerCluster)):
            X.append([random.normal(incomeCentroid, 10000.0), random.normal(ageCentroid,2.0)])
    X=np.array(X)
    return X
            