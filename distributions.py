import numpy as np
import matplotlib.pyplot as plt

values= np.random.uniform(-10.0,10.0, 100000)
plt.hist(values, 50)
plt.show()