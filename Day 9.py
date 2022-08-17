# Aim: Review of plotting line graphs in Python

from matplotlib import pyplot as plt

# Data Set
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [3, 6, 9, 12, 15]

# Using .plot() to plot, change colour of line and marker
plt.plot(x, y1, color = 'pink', marker = 'o')
plt.plot(x, y2, color = 'gray', marker = 'o')

# Changing the labels
plt.title("Title")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Adding Legend
plt.legend([x, y1, y2], loc=4)

# Displaying the graph
plt.show()