import matplotlib.pyplot as plt
import numpy as np

# fig = plt.figure() #empty figure

# plt.show() #show figure

# x1 = 1
# y1 = 1
# x2 = 5
# y2 = 5
# x3 = 3
# y3 = -2

# x_values = np.array([x1,x2,x3])
# y_values = np.array([y1,y2,y3])

# plt.plot(x_values, y_values, marker='v') # 'o' = circles, 's' = squares, '.' = small dots
# plt.show()

x = np.linspace(0,10,100) # creates 100 values evenly spread from 0 to 10
y1 = np.sin(x)
y2 = np.cos(x)

plt.figure(figsize=(6,4)) #define width and height in inches
 

plt.plot(x,y1, label='sine', color='Crimson', linestyle='-', marker='v') # linestyle defines the curve-style
plt.plot(x,y2, label='cosine', color='Green', linestyle='-.', marker='s')

plt.legend(loc='upper right') # shows labels in the upper right corner

plt.title('Unnecessary chart', loc='left', fontsize=24) # add title, left aligned
plt.xlabel('This is X-axis', fontsize=17) # Add label for x
plt.ylabel('This is Y-axis', fontsize=17) # Add label for y

plt.grid(True) # Show grid (duh)
plt.show()
