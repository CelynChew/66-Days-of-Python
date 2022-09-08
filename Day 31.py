# Aim: Selecting Rows

import pandas as pd

# Data Set
df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west'])

# Selecting row based on 'month' coloumn 
january = df[df.month == 'January']

# Finding months where 'clinic_east' has 51 patients
patients_51 = df[df.clinic_east == 51]

print(january)
print(patients_51)


# Selecting rows with 'or' (can also use '|')
march_april = df[(df.month == 'March') | (df.month == 'April')]

print(march_april)

# Selecting rows with 'and' (can also use '&')
june = df[(df.clinic_east == 112) & (df.clinic_west == 129)]

print(june)

# Selecting rows with 'isin' command
    # can use to minimise use of 'or'
january_february_march = df[df.month.isin(['January', 'February', 'March'])]

print(january_february_march)