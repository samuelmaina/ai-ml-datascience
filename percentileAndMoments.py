import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis

#generte random values 
vals= np. random. normal(0,0.5, 10000)

print(np.percentile(vals, 50))
print(np.percentile(vals, 90))
print(np.percentile(vals, 20))

#first moment
print(" The first moment" , np.mean(vals))

#second moment
print( "The second moment", np.var(vals))

#3rd moment
#used to show how values have skewed to towards
#one tail if the skew is to the right then that is negative skewness
#if the skewness is to the left , then that is positive skewness
print( "The third moment", skew(vals))


#it is used to get the high of the distribution.
print("The fourth moment", kurtosis(vals))


