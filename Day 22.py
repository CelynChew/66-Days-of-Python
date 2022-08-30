# Aim: Review on side by side bar chart

from matplotlib import pyplot as plt

# Data Set
unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
middle_school_a = [80, 85, 84, 83, 86]
middle_school_b = [73, 78, 77, 82, 86]

# Function to create list
def create_x(t, w, n, d):
    return [t*x + w*n for x in range(d)]
# Creating list with above function
school_a_x = create_x(2, 0.8, 1, 5)
school_b_x = create_x(2, 0.8, 2, 5)

# Creating a figure with width of 10 and height of 8
plt.figure(figsize=(10,8))
ax = plt.subplot()
# plotting bar graphs
plt.bar(school_a_x, middle_school_a)
plt.bar(school_b_x,middle_school_b)
middle_x = [(a + b) / 2.0 for a, b in zip(school_a_x, school_b_x)]

# Setting x ticks
ax.set_xticks(middle_x)
ax.set_xticklabels(unit_topics)

# Labeling graph and adding legends
plt.legend(["Middle School A", "Middle School B"])
plt.title('Test Averages on Different Units')
plt.ylabel('test average')
plt.xlabel('unit')
plt.show()

# Saving graph as jpeg file
plt.savefig('my_side_by_side.jpeg')