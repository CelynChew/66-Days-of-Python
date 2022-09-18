# Aim: Aggregating by Multiple Columns

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

iris = pd.read_csv("irisdata.csv")
print(iris)

sns.barplot(data = iris,
            x = 'Petal.Length',
            y = 'Sepal.Length',
            hue="Species")

plt.show()