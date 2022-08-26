# Aim: Plotting multiple histograms

from matplotlib import pyplot as plt

random_num1 = [2, 4, 6, 6, 4, 5]
random_num2 = [3, 4, 5, 8, 6, 5]

# Plot histograms using .hist(). if 'alpha' not used, second plot may completely cover first plot.
plt.hist(random_num1, bins=20, alpha = 0.4)
plt.hist(random_num2, bins = 20, alpha = 0.4)

plt.show()