from numpy import mean,dot
import matplotlib.pyplot as plt

import numpy as np


def de_mean(x):
    xmean= np.mean(x)
    return [x1 - xmean for x1 in x]

def coveriance(x, y):
    n= len(x)
    return np.dot(de_mean(x),de_mean(y))/(n-1)


pageSpeeds=np.random.normal(3.0, 1.0, 1000)
purchaseAmount= np.random.normal(50.0, 10.0, 1000)

plt.scatter(pageSpeeds,purchaseAmount)
plt.show()
print(coveriance(pageSpeeds, purchaseAmount))



def correlation(x, y):
    stddevx= x.std()
    stddevy= y.std()
    return coveriance(x, y)/stddevx/stddevy


print(correlation(pageSpeeds, purchaseAmount))




