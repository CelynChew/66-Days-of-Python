# Aim: Continuation of Day 7

from matplotlib import pyplot as plt

# Modifying Ticks
# Ticks are the values used to show specific points on the coordinate axis

# Saving .subplot() to variable 'ax'
ax = plt.subplot()

plt.plot([1, 3, 3.5], [0.1, 0.6, 0.8], 'o')
ax.set_yticks([0.1, 0.6, 0.8])
ax.set_yticklabels(['10%', '60%', '80%'])

# plt.show()


# .close('all') clears all exisiting plots
plt.close('all')

# Data set
power_generated = [753.9, 768.8, 780.1, 763.7, 788.5, 782, 787.2, 806.4, 806.2, 798.9]
years = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009]

# Use .figure() to size graph
# figsize = (width, height)
plt.figure(figsize=(10, 10))

plt.plot(years, power_generated)

# .savefig() saves graph as a file onto laptop
# plt.savefig('power_generated.png')
plt.show()