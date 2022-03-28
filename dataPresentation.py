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

#adjusting the axes values.
axes= plt.axes()
axes.set_xlim([-5, 5])
axes.set_ylim([0, 1.0])
axes.set_xticks([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])
axes.set_yticks([0,0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9 , 1.0])
plt.plot(x, norm.pdf(x))
plt.plot(x, norm.pdf(x, 1.0, 0.5))
plt.show()

#changing the line types and the colors

#create the a blue solid line
plt.plot(x, norm.pdf(x), "b-")
#create a red line that is broken
plt.plot(x, norm.pdf(x, 1.0, 0.5), "r:")
plt.show()

#labelling axes and adding legend
plt.xlabel("Greebles")
plt.ylabel("Probability")
plt.plot(x, norm.pdf(x), "b-")
plt.plot(x,norm.pdf(x,1.0, 0.5), "r:")
plt.legend(["Sneetches", "Gacks"], loc= 4)
plt.show()

#creating a pie chart
values= [12, 55, 4, 32, 14]
colors= ["r",'g', 'b', 'c', 'm']
explode= [0,0,0.2, 0, 0]
labels= ["Kenya", "Uganda", "Tanzania", "Burundi", "Rwanda"]
plt.pie(values,colors= colors, labels= labels, explode=explode)
plt.title("Student Location")
plt.show()



