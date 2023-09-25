import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

# Data
# fruits = ['bananas', 'pinapple', 'oranges','limes']
# number_of_fruits = [12,23,15,40]

# #Bar chart
# # plt.bar(fruits, number_of_fruits, color=['gold', 'brown', 'orange', 'green'])


# # Add labes
# # plt.xlabel('Fruits')
# # plt.ylabel('Number of fruits')
# # plt.title('Fruit consumption')


# # # #annoitions
# # plt.annotate("I added text", xy=(2,18), xytext=(2.1,18.1), arrowprops=dict(arrowstyle='<->', color='red'))

# colors = ['blue','green','red', 'purple']

# #Pie chart
# plt.pie(number_of_fruits, labels=fruits, colors=colors, autopct='%1.2f%%') #with percentages
# plt.show()

CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))

medals = pd.read_csv(CURR_DIR_PATH+'\\'+'London 2012 Olympic alternative medal rankings - ALL.csv')

countries_medals = medals[['Country name','Gold','Silver','Bronze','Total']]
countries_medals.set_index("Country name", inplace=True)
only_countries_medals = countries_medals.loc[(countries_medals!=0).any(axis=1)]
top_ten = only_countries_medals.nlargest(10, 'Total')

# top_ten[['Gold', 'Silver', 'Bronze']].plot(kind='bar', stacked=True, color=['gold', 'silver', 'saddlebrown'])
# plt.title('Top ten medals 2012')
# plt.xlabel('Country Name')
# plt.ylabel('Total')
# plt.show()

top_ten[['Bronze', 'Silver','Gold' ]].plot(kind='barh', stacked=True, color=['saddlebrown', 'silver', 'gold'])
plt.title('Top ten medals 2012')
plt.ylabel('Country Name')
plt.xlabel('Total')
plt.show()