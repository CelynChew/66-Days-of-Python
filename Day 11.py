# Aim: Plotting simple bar graph

from matplotlib import pyplot as plt

# Data set
drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales =  [91, 76, 56, 66, 52, 27]

# using .bar(x-axis, y-axis) to plot number of drinks on the x-axis and number of drinks sold on the y-axis 
#plt.bar(drinks, sales)
#plt.show()



# Alternative method:
drink = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
num_sold = [91, 76, 56, 66, 52, 27]

# using.bar() to plot bar graph like aboove
plt.bar(range(len(drink)), num_sold)

#create your ax object here
ax = plt.subplot()
ax.set_xticks(range(len(drink)))
ax.set_xticklabels(drink)

plt.show()