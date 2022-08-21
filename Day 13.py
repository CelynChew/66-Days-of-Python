# Aim: Plotting stacked bar plots

from matplotlib import pyplot as plt

# Data Set
drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales1 =  [91, 76, 56, 66, 52, 27]
sales2 = [65, 82, 36, 68, 38, 40]

# Use .bar() to plot a regular bar graph
plt.bar(range(len(sales1)), sales1)
# Use 'bottom =' to assign variable to bottom to form stacked bar plot
plt.bar(range(len(sales2)), sales2, bottom = sales1)

# Using .legend() to assign legends
plt.legend(['Sales 1', 'Sales 2'])

plt.show()