import numpy as np;
import matplotlib.pyplot as plt

#use the np module to generate 10,000 random data with normal distribution 
#with the mean of 27,000, with standard deviation of 15,000
incomes = np.random.normal(27000, 15000, 10000)

print(np.mean(incomes))

#generate a histogram with 50 strips
plt.hist(incomes,50)
plt.show()