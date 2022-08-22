# Aim: Plotting Error Bars

from matplotlib import pyplot as plt

# Data set
drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
ounces_of_milk = [6, 9, 4, 0, 9, 0]
error = [0.6, 0.9, 0.4, 0, 0.9, 0]

# 'yerr' shows error. 'capsize' controls caps size to aid with readability 
# plt.bar(range(len(ounces_of_milk)), ounces_of_milk, yerr = error, capsize = 5)

# Playing around with capsize
plt.bar(range(len(ounces_of_milk)), ounces_of_milk, yerr = error, capsize = 10)

plt.show()