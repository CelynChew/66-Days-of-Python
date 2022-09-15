# Aim: Modifying Error Bars with Seaborn

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

iris = pd.read_csv("irisdata.csv")

sns.barplot(data=iris, x="Species", y="Sepal.Length", errorbar="sd")
plt.show()