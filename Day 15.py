# Aim: Shade error are on line graphs

from matplotlib import pyplot as plt

# Data Set
months = range(12)
month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
revenue = [16000, 14000, 17500, 19500, 21500, 21500, 22000, 23000, 20000, 19500, 18000, 16500]

# Plotting normal line graph (revenue against months)
plt.plot(months, revenue)

# Changing x axis labels
ax = plt.subplot()
ax.set_xticks(months)
ax.set_xticklabels(month_names)

# Finding upper and lower bound for y value
y_lower = []
y_upper = []
for r in revenue:
  lower = 0.9 * r
  upper = 1.1 * r
  y_lower.append(lower)
  y_upper.append(upper)

# Using .fill_between(x-values, y_lower, y_upper, alpha = ) to shade the area. 'alpha' controls the shade of the shaded area. 
plt.fill_between(months, y_lower, y_upper, alpha = 0.2)

plt.show()