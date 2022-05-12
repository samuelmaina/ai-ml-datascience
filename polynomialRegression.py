import numpy as np

import matplotlib.pyplot as plt


pageSpeeds = np.random.normal(3.0, 1.0, 1000)

purchaseAmount = np.random.normal(50.0, 10.0, 1000) / pageSpeeds

plt.scatter(pageSpeeds, purchaseAmount)

# fit the data using 4th degree polynomial
x = np.array(pageSpeeds)
y = np.array(purchaseAmount)

p4 = np.poly1d(np.polyfit(x, y, 4))

xp = np.linspace(0, 7, 100)
plt.scatter(x, y)
plt.plot(xp, p4(xp), c="r")
plt.show()
