# Aim: Plotting histograms

from matplotlib import pyplot as plt

# Data Set
random_numbers = [2,3,4,5,4,3,6,4,5,7]

# plotting histogram with .hist(). 'range' selects the minimum and maximum values to plot. 'bins' displays the values divided into x number of bins. 
plt.hist(random_numbers, range = (3, 5), bins = 10)

plt.show()