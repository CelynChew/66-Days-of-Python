# Aim: Using Pandas for Seaborn

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

df = pd.read_csv('irisdata.csv')
print(df.head())

"""
Using sns.barplot() to plot a bar graph.
'data' -> data frame
'x' -> column that should be used for x-axis
y -> column that should be used for y-axis
"""
sns.barplot(
    data = df,
    x = 'Sepal.Width',
    y = 'Sepal.Length')

plt.show()