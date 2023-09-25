import matplotlib.pyplot as plt
import numpy as np

# # draw a smiley face or X**2
# # def x2(x):
# #     return x**2

# x = np.linspace(-10, 10, 100)
# # y = x2(x)

# # plt.plot(x,y)
# plt.plot(x,x**2)
# plt.show()


# # question 2
# x = np.linspace(-10, 10, 100)

# y = np.sin(x)

# plt.plot(x,y)
# plt.show()


# draw a star
plt.style.use('seaborn')
x_values = np.array([1,7,2,4,6,1])
y_values = np.array([4,4,1,6,1,4])

x2_values = np.array([1,7,2,4,6,1])
y2_values = np.array([5,5,2,7,2,5])

plt.plot(x_values, y_values, color="Red")
plt.plot(x_values, y_values, color="k", marker='o', linestyle='none') 
plt.plot(x2_values, y2_values, color="Blue")
plt.title("Twinkle little star", color="Red")

plt.show()