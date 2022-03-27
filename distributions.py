import numpy as np
import matplotlib.pyplot as plt

from scipy.stats import norm


#uniform distribution
values= np.random.uniform(-10.0,10.0, 100000)
plt.hist(values, 50)
plt.show()

#normal distribution
x= np.arange(-3,3, 0.0001)
plt.plot(x,norm.pdf(x));
plt.show()