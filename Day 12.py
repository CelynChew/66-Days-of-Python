# Aim: Plotting side by side bar charts

from matplotlib import pyplot as plt

# Data set
drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales1 =  [91, 76, 56, 66, 52, 27]
sales2 = [65, 82, 36, 68, 38, 40]

# Paste the x_values code here
n = 1  # First dataset (out of 2)
t = 2 # Number of datasets
d = 6 # Number of sets of bars
w = 0.8 # Width of each bar
store1_x = [t * element + w * n for element in range(d)]

plt.bar(store1_x, sales1)

n = 2  # Second dataset (out of 2)
t = 2 # Number of datasets
d = 6 # Number of sets of bars
w = 0.8 # Width of each bar
store2_x = [t * element + w * n for element in range(d)]

plt.bar(store2_x, sales2)

plt.show()