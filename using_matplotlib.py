import matplotlib.pyplot as plt
import numpy as np

# fig = plt.figure() #empty figure

# plt.show() #show figure

x1 = 1
y1 = 1
x2 = 5
y2 = 5
x3 = 3
y3 = -2

x_values = np.array([x1,x2,x3])
y_values = np.array([y1,y2,y3])

plt.plot(x_values, y_values)
plt.show()