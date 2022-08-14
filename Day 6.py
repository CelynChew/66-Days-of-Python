# Aim: Continuation of day 5

from matplotlib import pyplot as plt

# Creating subplots
# Arguments needed for subplots -> .subplot(no. of rows of subplots, no. of columns of subplots, index of the subplot we want to create)

# Data sets
x = [1, 2, 3, 4]
y = [1, 2, 3, 4]
 
# First Subplot
plt.subplot(1, 2, 1)
plt.plot(x, y, color='green')
plt.title('First Subplot')
 
# Second Subplot
plt.subplot(1, 2, 2)
plt.plot(x, y, color='blue')
plt.title('Second Subplot')
 
# Display both subplots
# plt.show()


# Customising subplots with .subplots_adjust()
"""
left — the left-side margin, with a default of 0.125. You can increase this number to make room for a y-axis label
right — the right-side margin, with a default of 0.9. You can increase this to make more room for the figure, or decrease it to make room for a legend
bottom — the bottom margin, with a default of 0.1. You can increase this to make room for tick mark labels or an x-axis label
top — the top margin, with a default of 0.9
wspace — the horizontal space between adjacent subplots, with a default of 0.2
hspace — the vertical space between adjacent subplots, with a default of 0.2
"""
x = range(7)
straight_line = [0, 1, 2, 3, 4, 5, 6]
parabola = [0, 1, 4, 9, 16, 25, 36]
cubic = [0, 1, 8, 27, 64, 125, 216]

# First subplot
plt.subplot(2,1,1)
plt.plot(x, straight_line)

# Second subplot
plt.subplot(2, 2, 3)
plt.plot(x, parabola)

# Third subplot
plt.subplot(2, 2, 4)
plt.plot(x, cubic)

# For before and after comparison
# plt.show()

# Customising plot
plt.subplots_adjust(wspace = 0.35, bottom = 0.2)

plt.show()
