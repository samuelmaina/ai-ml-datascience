import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt


#showing a single graph on some axis
plt.xlabel("Incomes")
plt.ylabel("No of values")
x= np. arange(-3, 3, 0.001)
plt.plot(x,norm.pdf(x))
plt.show()

#multiple plots on the same graph
plt.xlabel("Incomes")
plt.ylabel("No of values")

plt.plot(x,norm.pdf(x))
plt.plot(x, norm.pdf(x, 1.0, 0.5))
plt.show()

#saving the content into a file
plt.xlabel("Incomes")
plt.ylabel("No of values")
plt.plot(x, norm.pdf(x))
plt.plot(x, norm.pdf(x, 1.0, 0.5))
plt.savefig("myPlot.png", format= "png")




