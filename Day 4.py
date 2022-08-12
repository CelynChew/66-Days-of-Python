# Aim: Learn List Comprehensions

temperatures = [-5, 29, 26, -7, 1, 18, 12, 31]

# increasing each temperature by 20 degrees
temperatures_manually_adjusted = [15, 49, 46, 13, 21, 38, 22, 51]
print(temperatures_manually_adjusted)

# using list comprehensions to adjust all temperatures
# [formula for item in list]
temperatures_adjusted_by_list_comprehension = [temp + 20 for temp in temperatures]
print(temperatures_adjusted_by_list_comprehension)

# using loop to achieve the same result
temperatures_adjusted_by_loop = []
for t in temperatures:
    t += 20
    temperatures_adjusted_by_loop.append(t)
print(temperatures_adjusted_by_loop)