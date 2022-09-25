# Aim: Finding avaerages between decades and putting them into arrays

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

def get_averages(months, rain, first, last):
    selected_months = np.arange(first, last, dtype = 'datetime64[M]')
    
    index = []
    for date in selected_months:
        if date in months:
            index.append(np.where(months == date))
    if len(index) == 0:
        return ValueError, print("No data in date range")
    
    rainfall = []
    for i in index:
        rainfall.append(rain[i])
    
    average = sum(rainfall) / len(rainfall)
    avs = np.full([len(index)], average, dtype = float)
    return selected_months, avs

def all_decades(months, rain):
    decades = np.arange(months[0], months[-1] + (12 * 10), dtype = 'datetime64[10Y]')
    
    mean_ys = np.array([])
    count = 0
    while count < len(decades) - 1:
        first = decades[count]
        last = decades[count + 1]
        
        averages = list(get_averages(months, rain, first, last)[1])
        mean_ys = np.append(mean_ys, averages)
        
        count += 1
        
    return months, mean_ys

print(all_decades(raindata(airport_data)[0], raindata(airport_data)[1]))