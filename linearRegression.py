import numpy as np

from scipy import stats

import matplotlib.pyplot as plt


pageSpeeds= np.random.normal(3.0, 1.0, 1000)
purchases= 100*(pageSpeeds +np.random.normal(0, 0.1, 1000))*3

plt.scatter(pageSpeeds, purchases)


slope, intersept, r_value, p_value, std_err= stats.linregress(pageSpeeds, purchases)

print(r_value**2)

def predict(x):
    return slope* x + intersept

fitLine= predict(pageSpeeds)
plt.plot(pageSpeeds,fitLine, c='r')
plt.show()

