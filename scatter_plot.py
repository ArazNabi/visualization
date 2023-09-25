import matplotlib.pyplot as plt
import numpy as np


# # Create a scatter plot of random data point

# x = np.random.rand(50)
# y = np.random.rand(50)

# plt.scatter(x,y)

# ax = plt.gca() # get current axis
# ax.spines['top'].set_visible(False) # Hide spine(frame-line)
# ax.spines['right'].set_visible(False) # Hide spine(frame-line)
# plt.show()

def create_weight(n):
    return np.random.randint(55,116, n)

def create_height(n):
    return np.random.uniform(low=1.45, high=2.10, size=n)


def create_physique(n):
    height = create_height(n)
    weight = create_weight(n)
    bmi = weight / (height * height)
    return weight,height,bmi

weight, height, bmi =create_physique(100)

for i in range(100):
    if bmi[i] < 18.5 or bmi[i] > 25:
        plt.scatter(weight[i], height[i], color='red')
    else:
        plt.scatter(weight[i], height[i], color='green')

plt.title("BMI")
plt.show()