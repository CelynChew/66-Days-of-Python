# Aim: Load, save and inspect CSVs with pandas

import pandas as pd

df = pd.read_csv('irisdata.csv')

# .head() gives the first 5 rows of the data frame
first_5_rows = df.head()

# .head(10) gives the first 10 rows of the data frame
first_10_rows = df.head(10)

# .info() gives general information about each column
info = df.info()

print(df)
print(first_5_rows)
print(first_10_rows)