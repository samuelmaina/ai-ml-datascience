import numpy as np
import matplotlib.pyplot as plt

from scipy.stats import norm, binom, expon, poisson


#uniform 
values= np.random.uniform(-10.0,10.0, 100000)
plt.hist(values, 50)
plt.show()

#normal (Probability Density Function)
x= np.arange(-3,3, 0.0001)
plt.plot(x,norm.pdf(x));
plt.show()

#exponential (pdf)
x= np.arange(0,10,0.0001)
plt.plot(x,expon.pdf(x))
plt.show()


#binomial (Probability mass function)
n,p = 10, 0.5
x= np.arange(0,10, 0.001)
plt.plot(x, binom.pmf(x,n,p))
plt.show()

#poisson (PMF)

mu= 500
x= np.arange(400, 600, 0.5)
plt.plot(x, poisson.pmf(x,mu))
plt.show()




