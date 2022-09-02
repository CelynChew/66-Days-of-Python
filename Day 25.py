# Aim: Review on labeled pie chart

from matplotlib import pyplot as plt

# Date set
unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
num_hardest_reported = [1, 3, 10, 15, 1]

plt.figure(figsize=(10,8))
plt.pie(num_hardest_reported, labels=unit_topics, autopct="%1d%%")

plt.axis('equal')
plt.title('Hardest Topics')

plt.show()
plt.savefig("my_pie_chart.png")
