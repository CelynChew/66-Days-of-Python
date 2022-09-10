# Aim: Review of pandas

import pandas as pd

iris = pd.read_csv('irisdata.csv')

head = iris.head()
print(head)


length = iris['Sepal.Length']
print(length)


setosa = iris[(iris.Species == 'Setosa')]
print(setosa)