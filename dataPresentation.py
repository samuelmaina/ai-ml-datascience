import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt


#showing a single graph on the same axes
x= np. arange(-3, 3, 0.001)
plt.plot(x,norm.pdf(x))
plt.show()