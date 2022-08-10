# Aim: Refresh on if and else statements

#calculating population growth in a city
def population_growth(year_one, year_two, population_one, population_two):
    # using if and else statements to ensure that numbers are positive
    if population_one > population_two:
        population_change = population_one - population_two
    else:
        population_change = population_two - population_one

    if year_one > year_two:
        percentage_growth = (population_change/population_two) * 100
        growth_rate = percentage_growth / (year_one - year_two)
    else: 
        percentage_growth = (population_change/population_one) * 100
        growth_rate = percentage_growth / (year_two - year_one) 
  
    return growth_rate

set_one = population_growth(2017, 1927, 15029231, 691000)

report = 'The annual growth rate from 1972 to 2017 is ' + str(round(set_one,1)) + '%.'
print(report)


# checking the above function with manual calculations
pop_1927 = 691000
pop_2017 = 15029231

pop_change = pop_2017 - pop_1927
# percentage growth rate
percentage_gr = ((pop_change)/pop_1927) * 100

# annual percentage growth
annual_gr = percentage_gr / (2017 - 1927)
print(annual_gr)