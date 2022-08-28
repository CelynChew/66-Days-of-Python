# Aim: Spreading out numbers when a range of age is given

def spread(age_cat, num):
    smallest = youngest = int(age_cat[7:age_cat.index('_', 7)])
    largest = int(age_cat[age_cat.index('_', 7) + 1:])

    ages = []
    while youngest <= largest:
        ages.append(str(youngest))
        youngest += 1

    i = 0
    for age in ages:
        age = 'Age_yr_' + age
        ages[i] = age
        i += 1

    i = 0
    sprd = []
    if num % (largest - smallest + 1) == 0:
        while i <= (largest - smallest):
            sprd.append(int(num / (largest - smallest)))
            i += 1
        return ages, sprd

    else:
        remainder = num % (largest - smallest + 1)
        base = num - remainder
        while len(sprd) != len(ages):
            sprd.append(int(base / len(ages)))

        while remainder > 0:
            sprd[i] += 1
            i += 1
            remainder = remainder - 1

        return ages, sprd
    
print(spread('Age_yr_80_84', 7))