# Aim: Review on plotting bar chart with error

from matplotlib import pyplot as plt

# Data Set
past_years_averages = [82, 84, 83, 86, 74, 84, 90]
years = [2000, 2001, 2002, 2003, 2004, 2005, 2006]
error = [1.5, 2.1, 1.2, 3.2, 2.3, 1.7, 2.4]

# Creating a figure with a width of 10 and height of 8
plt.figure(figsize=(10,8))

# Adding error bars
plt.bar(range(len(past_years_averages)), past_years_averages, yerr = error, capsize=5)
# Adjusting axis
plt.axis([-0.5, 6.5, 70, 95])

# Changing x ticks
ax = plt.subplot()
ax.set_xticks(range(len(years)))
ax.set_xticklabels(years)

# Labeling the graph
plt.title('Final Exam Averages')
plt.ylabel('Test average')
plt.xlabel('Year')

# Saving graph as an image
plt.savefig('my_bar_chart.jpeg')
plt.show()