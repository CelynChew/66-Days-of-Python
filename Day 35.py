# Aim: Performing Column Operations and Renaming Columns

import pandas as pd

# Function to change strings to lowercase
def lowercase(my_string):
  return my_string.lower()

# Data set
df = pd.DataFrame([
  ['JOHN SMITH', 'john.smith@gmail.com'],
  ['Jane Doe', 'jdoe@yahoo.com'],
  ['joe schmo', 'joeschmo@hotmail.com']
],
  columns=['Name', 'Email']
)

# Adding new columns with all names changed to lower case
df['Lowercase Name'] = df['Name'].apply(lowercase)
print(df)

# Renaming columns (Method 1)
df.columns = ['Names', 'Email Address', 'Names in Lowercase']
print(df)

# Renaming columns (Method 2)
# 'inplace = True' edits the original data frame
df.rename(columns = {'Email Address': 'Email'}, inplace = True)
print(df)