# Aim: Setting indices with pandas

import pandas as pd

# Data set
df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west']
)

# Making a new dataframe that only contains months 'February', 'April' and 'June'
df2 = df.loc[[1, 3, 5]]
print(df2)


df3 = df2.reset_index()
print(df3)

# without 'drop = True', original index is moved into a new column. Unless those indexes are needed, it is better to drop them so that we don't end up with an extra column.
df4 = df2.reset_index(drop = True)
print(df4)
