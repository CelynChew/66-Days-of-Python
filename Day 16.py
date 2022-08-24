# Plotting Pie Chart

from matplotlib import pyplot as plt

# Data set
payment_method_names = ["Card Swipe", "Cash", "Apple Pay", "Other"]
payment_method_freqs = [270, 77, 32, 11]

# .pie() plots the pie chart. 'labels' label the different sections. 'autopct' adds the percentage of the total that each slice occupies.
"""
'%0.2f' — 2 decimal places, like 4.08
'%0.2f%%' — 2 decimal places, but with a percent sign at the end, like 4.08%. You need two consecutive percent signs because the first one acts as an escape character, so that the second one gets displayed on the chart.
'%d%%' — rounded to the nearest int and with a percent sign at the end, like 4%.
"""
plt.pie(payment_method_freqs, labels = payment_method_names, autopct = '%0.1f%%')
# .axis('equal') makes it look flat rather than tilted.
plt.axis('equal')

# Alternative method to label
plt.legend(payment_method_names)

plt.show()