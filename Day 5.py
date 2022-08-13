# Aim: Learn to plot graphs in Python using matplotlib

from matplotlib import pyplot as plt

x_values = [0, 1, 2, 3, 4]
y_values = [0, 1, 4, 9, 16]
# .plot() createes graph
#plt.plot(x_values, y_values)
# .show() displays graph
#plt.show()


# plotting 2 lines on the same graph
time = [0, 1, 2, 3, 4]
revenue = [200, 400, 650, 800, 850]
costs = [150, 500, 550, 550, 560]

#plt.plot(time, revenue)
#plt.plot(time, costs)

# customising lines
#plt.plot(time, revenue, color = 'purple', linestyle = '--')
#plt.plot(time, costs, color = '#82edc9', marker = 's')

#plt.show()


# .axis() controls the range displayed on the axis
x = [0, 1, 2, 3, 4]
y = [0, 1, 4, 9, 16]
#plt.plot(x, y)
#plt.axis([0, 3, 2, 5])
#plt.show()


# Labeling Axes
hours = [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
happiness = [9.8, 9.9, 9.2, 8.6, 8.3, 9.0, 8.7, 9.1, 7.0, 6.4, 6.9, 7.5]

plt.plot(hours, happiness)

# .xlabel() gives the x axis a title
plt.xlabel('Time of day')
# .ylabel() gives the y axis a title
plt.ylabel('Happiness Rating (out of 10)')
# .title() gives the graph a title
plt.title('My Self-Reported Happiness While Awake')
plt.show()