# Aim: Refresh on lists

example_list = [1, 2, 3, 4]

# Using Append
example_list.append(5)
# print(example_list)

# Using Remove
example_list.remove(5)

# print(example_list)


flowers = ["daisies", "periwinkle"]

#Try to append more than one item
# flowers.append("tulips", "roses") -> causes error. append only takes one argument
flowers.append("tulips")
flowers.append("roses")

# print(flowers)


# Growing list using '+':
flowers1 = ["daisy", "buttercup", "snapdragon", "gardenia", "lily"]

# Create new orders here:
flowers2 = ["lilac", "iris"]
flowers_combined = flowers1 + flowers2
# print(flowers_combined)


# Accessing list elements:
names = ["Michael", "Dwight", "Jim", "Pam", "Ryan", "Andy", "Robert"]
# print(names[3])

# Using negative index
shopping_list = ["eggs", "butter", "milk", "cucumbers", "juice", "cereal"]
last_element = shopping_list[-1]
second_last_element = shopping_list[-2]
# print(last_element, second_last_element)


# Modifying lists:
garden_waitlist = ["Jiho", "Adam", "Sonny", "Alisha"]

garden_waitlist[1] = "Calla"
# print(garden_waitlist)

garden_waitlist[-1] = "Alex"
# print(garden_waitlist)


# Accessing element 2-dimensional list:
class_name_test = [["Jenny", 90], ["Alexus", 85.5], ["Sam", 83], ["Ellie", 101.5]]
# print(class_name_test)

sams_score = class_name_test[2][1]
# print(sams_score)

ellies_score = class_name_test[-1][-1]
# print(ellies_score)


# Modifying 2-dimensional list:
class_list = [["Kenny", "American", 9], ["Tanya", "Russian", 9], ["Madison", "Indian", 7]]
# print(class_list)

class_list[2][2] = 8
# print(class_list)

class_list[-3][-3] = "Ken"
# print(class_list)

# Using remove for 2-dimensional list:
class_list[1].remove(9)
# print(class_list)
