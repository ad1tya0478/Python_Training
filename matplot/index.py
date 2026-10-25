# Plot customization using matplotlib

# import matplotlib.pyplot as plt
# import numpy as np

# x = np.array([2023, 2024, 2025, 2026])
# y1 = np.array([15,25,30,20])
# y2 = np.array([17,23,38,5])
# y3 = np.array([13,15,20,16])

# line_style = dict(marker=".", markersize=30, markerfacecolor="cyan", markeredgecolor="black", linestyle="solid", linewidth=4)

# plt.plot(x, y1, color="cyan",**line_style)

# plt.plot(x, y2, color="red", **line_style)

# plt.plot(x, y3, **line_style)

# plt.show()


# labels ------------------

# import matplotlib.pyplot as plt
# import numpy as np

# x = np.array([2023, 2024, 2025, 2026])
# y1 = np.array([15,25,30,20])
# y2 = np.array([17,23,38,5])
# y3 = np.array([13,15,20,16])

# plt.title("Class Size", fontsize=20, family="Arial", fontweight="bold", color="#2d4cfc")

# plt.xlabel("Year", fontsize=20, family="Arial", fontweight="bold", color='#2dbefc')
# plt.ylabel("Students", fontsize=20, family="Arial", fontweight="bold", color='#2dbefc')

# plt.tick_params(axis="both", color="#2dbefc")

# plt.plot(x, y1)
# plt.plot(x, y2)
# plt.plot(x, y3)

# plt.xticks(x)

# plt.show()


# gird lines -------------------------
# gird() = helps make plots easier to read by adding reference lines.

# import matplotlib.pyplot as plt
# import numpy as np

# x = [1,2,3,4,5]
# y = [5, 10, 15, 20, 25]

# plt.grid(axis="both", linewidth=2, color="lightgrey", linestyle="dashed")
# plt.plot(x, y)
# plt.show()


# bar chart ----------------
# bar chart - compares categories of data by representing each category with a bar 

# import numpy as np 
# import matplotlib.pyplot as plt

# categories = np.array(["Grains", "Fruit", "Vegetables", "Protien", "Dairy", "Sweets"])
# values = np.array([4,3,2,5,3,1])

# plt.bar(categories, values, color="skyblue")
# plt.title("Daily Consumption")
# plt.xlabel("Food")
# plt.ylabel("Quantity")

# plt.show()


# pie chart -----------
# pie chart - Circular chart divied into slices to show percentages of the total. Good for visualizing distribution among categories.

# import matplotlib.pyplot as plt
# import numpy as np

# categories = np.array(["Freshmen", "Sophomores", "Juniors", "Seniors"])
# values = np.array([300,250,275,225])
# colors = ["red", "yellow", "blue", "green"]

# plt.pie(values, labels=categories, autopct="%1.1f%%", colors=colors, explode=[0,0,0,0.1], shadow=True, startangle=90)
# plt.title("ITM University")

# plt.show()


# scatter plots -------------------------
# scatter graph - shows the relationship between two variables. Helps to identify a correlation(+,-,None). example: study hours vs Test scores 

# import numpy as np
# import matplotlib.pyplot as plt 

# x1 = np.array([0,1,1,2,3,4,5,6,7,7,8])
# y1 = np.array([55,60,65,62,68,70,75,78,82,85,87])

# x2 = np.array([0,1,2,2,3,4,5,6,7,8,8])
# y2 = np.array([50,58,65,70,72,78,83,88,92,95,97])

# plt.scatter(x1, y1, color="skyblue", alpha=0.5, s = 200, label="Class A")

# plt.scatter(x2, y2, color="red", alpha=0.5, s = 200, label="Class B")

# plt.title("Test Scores")
# plt.xlabel("Hours Studied")
# plt.ylabel("Grade")

# plt.legend()
# plt.show()


# Histograms -------------------
# - A visual representation of the distribution of quantitative data. They group values into bin(intervals) and counts how many fall in each range.

# import numpy as np
# import matplotlib.pyplot as plt 

# scores = np.random.normal(loc=80, scale=10, size=100)
# scores = np.clip(scores, 0, 100)


# plt.hist(scores, bins=10, color="lightgreen", edgecolor="black")

# plt.title("Exam Scores")
# plt.xlabel("Score")
# plt.ylabel("Number of students")

# plt.show()


# subplots ------------------------

# Figure = the entire canvas
# Ax = A single plot (subplot)
# import numpy as np
# import matplotlib.pyplot as plt

# x = np.array([1,2,3,4,5])

# figure, axes = plt.subplots(2,2)

# axes[0,0].plot(x, x*2, color="red")
# axes[0,0].set_title("x*2")

# axes[0,1].bar(x, x**2, color="blue")
# axes[0,1].set_title("x**2")

# axes[1,0].scatter(x, x**3, color="green")
# axes[1,0].set_title("x**3")

# axes[1,1].plot(x, x**4, color="yellow")
# axes[1,1].set_title("x*4")

# plt.tight_layout()
# plt.show()


# pandas + matplotlib ---------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("/mnt/Ad1Here/Python/Data File/data.csv")

type_count = df["Type1"].value_counts(ascending=True)

plt.barh(type_count.index, type_count.values, color="skyblue", edgecolor="black")
plt.title("Number of Pokemon by Types")
plt.xlabel("Count")
plt.ylabel("Type")
plt.tight_layout()
plt.show()