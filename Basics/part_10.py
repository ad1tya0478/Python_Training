import matplotlib.pyplot as plt
import seaborn as sns 
import numpy as np 
import pandas as pd

data = {
    "Category" : ['Laptop','Mouse','Keyboard','Monitor','Headphones'],
    "Revenue" : [50000,18000,90000,25000,12000],
    "Profit" : [12000,7000,5000,2000,4000],
    'Quantity': [5,50,40,10,35],
}

# Line plot - To visualize trend over time or continous data. Why : shows how values change sequentially

plt.figure(figsize=(6,4))
# print(plt.plot(data['Category'],data['Revenue']))

# plt.show()

# sns.barplot(x='Category',y='Revenue',data= data)
# plt.title("Seaborn Bar plot - Revenue By Category")

# print(plt.show())

# Histogram
# plt.figure(figsize=(6,4))
# plt.hist(data['Profit'], bins=10, color='Orange')
# plt.title("Histogram")
# plt.xlabel("Revenue")
# plt.ylabel("Frequency")
# print(plt.show())

# seaborn version
# sns.boxplot(x='Revenue', data=data)
# plt.title("Seaborn box plot - Revenue Distribution")
# plt.tight_layout()
# print(plt.show())

# Area Plot

x = np.arange(1,6)
y1 = np.array([10,20,30,25,15])
y2 = np.array([5,15,25,20,10])

plt.figure(figsize=(6,4))
plt.stackplot(x, y1, y2, labels=['Product A', 'Product B'])
plt.legend(loc='upper left')
print(plt.show())

