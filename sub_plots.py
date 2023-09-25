import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1,10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = x
y4 = x**2

plt.figure(figsize=(6,5))

# Subplot
# Subplot 1:sine curve

plt.subplot(2,2,1) # 2 x, 2y, position 1
plt.plot(x,y1, color='blue')
plt.title("Sine curve") #title for certain box

#Subplot 2: cosine
plt.subplot(2,2,2) # 2 x, 2y, position 2
plt.plot(x,y2, color='crimson')
plt.title("Cosine curve")

#Subplot 3: linear
plt.subplot(2,2,3) # 2 x, 2y, position 3
plt.plot(x,y3, color='pink')
plt.title("linear")

#Subplot 4:quadratic
plt.subplot(2,2,4) # 2 x, 2y, position 4
plt.plot(x,y4, color='purple')
plt.title("quadratic")

#Adjust spacing
plt.tight_layout()

# Title for all of it
plt.suptitle('Look at theese four things', fontsize=19)
# Adjust spacing above or below,left, right (can use plt.tight_layout in the end too)
plt.subplots_adjust(top=0.8) #80% from the bottom-left

plt.show()