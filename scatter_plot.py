import matplotlib.pyplot as plt
import numpy as np


# Create a scatter plot of random data point

x = np.random.rand(50)
y = np.random.rand(50)

plt.scatter(x,y)
plt.show()