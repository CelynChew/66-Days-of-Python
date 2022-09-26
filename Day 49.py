# Aim: Extracting data with 2-d arrays

import numpy as np

def year_range(town):
    data = np.array(np.genfromtxt(temperature_file(town), delimiter = ",", skip_header = 1, usecols = range(2, 16)))
    earliest = data[0,0]
    latest = data[-1,0]
    return earliest, latest