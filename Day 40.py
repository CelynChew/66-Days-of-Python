# Aim: Calculating Aggregates with Seaborn

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

iris = pd.read_csv("irisdata.csv")
print(iris)

sns.barplot(data = iris,
            x = 'Species',
            y = 'Sepal.Length',
            estimator=np.median)

plt.show()