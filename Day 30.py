# Aim: Selecting Multiple Columns and Rows with pandas

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

"""
 Selecting Multiple Columns
 <dataframe name>[[<columns wanted>]]
  note that there needs to be 2 sets of []
"""
clinic_north_south = df[['clinic_north', 'clinic_south']]

print(df)
print(clinic_north_south)

"""
 Selecting Rows
 <dataframe name>.iloc[<row number>]
"""
march = df.iloc[2]
april_may_june = df.iloc[3:6]
june = df.iloc[-1]

print(march)
print(april_may_june)
print(june)