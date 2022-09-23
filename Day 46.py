# Aim: Cleaning data and putting information into array

import numpy as np
from matplotlib import pyplot as plt
import csv

airport_data = "IDCJAC0001_009021_Data1.csv"

def raindata(site):
    with open(site, 'r') as f:
        file = csv.reader(f)
        lines = []
        for f in file:
            lines.append(f)
        
        header = lines[0]
        data = lines[1:]
        
        cleaned_data = []
        for d in data:
            if d[-2] != '' and d[-2][0] in '1234567890' and d[-1] in 'YN':
                cleaned_data.append(d)
                
        date_list = []
        rain_list = []
        flags_list = []
        for index, body in enumerate(cleaned_data):
            date_list.append(body[2] + '-' + body[3])
            rain_list.append(body[4])
            if body[5] == 'Y':
                flags_list.append(True)
            if body[5] == 'N':
                flags_list.append(False)
        months = np.full([len(date_list)], date_list, dtype = 'datetime64[M]')
        rain = np.full([len(rain_list)], rain_list, dtype = float)
        np.set_printoptions(formatter = {'float_kind':'{:.1f}'.format})
        flags = np.full([len(flags_list)], flags_list, dtype = bool)
        return months, rain, flags

print(raindata(airport_data))