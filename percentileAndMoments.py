import numpy as np
import matplotlib.pyplot as plt

#generte random values 
vals= np. random. normal(0,0.5, 10000)

print(np.percentile(vals, 50))
print(np.percentile(vals, 90))
print(np.percentile(vals, 20))