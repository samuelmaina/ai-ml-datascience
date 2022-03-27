import numpy as np;
import matplotlib.pyplot as plt

#use the np module to generate 10,000 random data with normal distribution 
#with the mean of 27,000, with standard deviation of 15,000
incomes = np.random.normal(27000, 15000, 10000)

print(np.mean(incomes))



print(np.median(incomes))

#Median is less suspectible to outliers than mean.


#the append method is used to concatenate two arrays 
original_incomes= incomes
incomes= np.append(incomes,[10000000000])

#the first run of the program the mean was 1026988.1125744453 and the median is 26929.598072966848 in which 26929 is more close
#to the center than the mean.
print("this is the mean affter outlier" ,np.mean(incomes))
print("This is the median after adding an outlier",np.median(incomes))


#generate random 500 integers from 18 to an upperbound of 90
ages= np.random.randint(18, high=90, size=500)
print(ages)

#generate a histogram with 50 strips
plt.hist(original_incomes,50)
plt.show()