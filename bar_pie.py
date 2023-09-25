import matplotlib.pyplot as plt


# Data
fruits = ['bananas', 'pinapple', 'oranges','limes']
number_of_fruits = [12,23,15,40]

#Bar chart
# plt.bar(fruits, number_of_fruits, color=['gold', 'brown', 'orange', 'green'])


# Add labes
# plt.xlabel('Fruits')
# plt.ylabel('Number of fruits')
# plt.title('Fruit consumption')


# # #annoitions
# plt.annotate("I added text", xy=(2,18), xytext=(2.1,18.1), arrowprops=dict(arrowstyle='<->', color='red'))

colors = ['blue','green','red', 'purple']

#Pie chart
plt.pie(number_of_fruits, labels=fruits, colors=colors, autopct='%1.2f%%') #with percentages
plt.show()