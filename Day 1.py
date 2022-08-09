# Aim: Refresh on Functions

# Part 1: Converting Temperature from fahrenheit to celsius and vice versa. 
def f_to_c(f_temp):
    c_temp = (f_temp -32) * 5/9
    return c_temp

f100_in_celsius = f_to_c(100)
print("100 fahrenheit is equal to " + str(round(f100_in_celsius,1)) + " celsius")


def c_to_f(c_temp):
    f_temp = c_temp * (9/5) + 32
    return f_temp

c0_in_fahrenheit = c_to_f(0)
print("0 celsius is equal to " + str(round(c0_in_fahrenheit, 1)) + " fahrenheit")


# Part 2: Using Functions to use the formula "Work = Force × Distance"
train_mass = 22680
train_acceleration = 10
train_distance = 100

def get_force(mass, acceleration):
    return mass * acceleration

train_force = get_force(train_mass, train_acceleration)

print("The train supplies " + str(train_force) + " Newtons of force.")

def get_work(mass, acceleration, distance):
    # calling get_force function in get_work function
    force = get_force(mass, acceleration)
    work = force * distance
    return work

train_work = get_work(train_mass,train_acceleration, train_distance)

print("The train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters")