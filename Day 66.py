def clean(table):
    data_without_nan = [d for d in table if np.isnan(d[-1]) == False]
    
    calculated_mean = []
    reported_mean = []
    for d in data_without_nan:
        calculated_mean.append(np.mean(d[1:-1]))
        reported_mean.append(d[-1])
    calculated_mean = np.array(calculated_mean)
    reported_mean = np.array(reported_mean)
    
    mask = np.isclose(calculated_mean, reported_mean, rtol = 0.15)
    cleaned = np.array(data_without_nan)[mask]
    return cleaned