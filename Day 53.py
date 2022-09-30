# Aim: Finding euclidean, manhattan, and hamming distance with scipy.
# And finding better model with help of loss

from scipy.spatial import distance

# euclidean distance
print(distance.euclidean([1, 2], [4, 0]))

# manhattan distance
print(distance.cityblock([1, 2], [4, 0]))

# hamming distance
print(distance.hamming([5, 4, 9], [1, 7, 9]))


x = [1, 2, 3]
y = [5, 1, 3]

# linear equation: y = x
m1 = 1
b1 = 0

# linear equation: y = 0.5x + 1
m2 = 0.5
b2 = 1

y_predicted1 = [m1*x_val + b1 for x_val in x]
y_predicted2 = [m2*x_val + b2 for x_val in x]

total_loss1 = 0
total_loss2 = 0

for i in range(len(y)):
  total_loss1 += (y[i] - y_predicted1[i])**2
  total_loss2 += (y[i] - y_predicted2[i])**2
  
print(total_loss1, total_loss2)
#better_fit = 2