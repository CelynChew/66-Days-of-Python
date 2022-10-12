def validate_averages():
    towns, data = get_temperatures(STATIONS)
    reported_mean = []
    calculated_mean = []
    year = []
    for arrs in data:
        for d in arrs:
            reported_mean.append(d[-1])
            year.append(d[0])
            calculated_mean.append(np.around(np.mean(d[1:-1]), decimals = 1))
    reported_mean = np.array(reported_mean)
    calculated_mean = np.array(calculated_mean)
    year = np.array(year)
    
    isclose = np.isclose(reported_mean, calculated_mean)
    indexes_of_not_close = np.where(isclose == False)
    
    years_not_close = year[indexes_of_not_close]
    reported_mean_not_close = reported_mean[indexes_of_not_close]
    calculated_mean_not_close = calculated_mean[indexes_of_not_close]
    
    mismatch = np.stack((years_not_close, reported_mean_not_close, calculated_mean_not_close), axis = 1)
    return mismatch
