# Aim: Adding Columns with pandas

import pandas as pd

df = pd.DataFrame([
  [1, '3 inch screw', 0.5, 0.75],
  [2, '2 inch nail', 0.10, 0.25],
  [3, 'hammer', 3.00, 5.50],
  [4, 'screwdriver', 2.50, 3.00]
],
  columns=['Product ID', 'Description', 'Cost to Manufacture', 'Price']
)
print(df)

# Adding Column
df['Sold in Bulk?'] = ['Yes', 'Yes', 'No', 'No']
print(df)

# Adding Column where all rows have same value
df['Is Taxed?'] = 'Yes'
print(df)

# Adding Column by performing an operation on existing columns
df['Revenue'] = df['Price'] - df['Cost to Manufacture']
print(df)