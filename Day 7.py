# Aim: Continuation of day 6

from matplotlib import pyplot as plt

# Displaying legend using .legend()
plt.plot([0, 1, 2, 3, 4], [0, 1, 2, 3, 4])
plt.plot([0, 1, 2, 3, 4], [0, 1, 8, 27, 64])
# plt.legend(['linear', 'cubic'])
# plt.show()

# Positioning legend using loc
"""
Number Code	   String
0	           best
1	           upper right
2	           upper left
3	           lower left
4	           lower right
5	           right
6	           center left
7	           center right
8	           lower center
9	           upper center
10	           center
"""
#plt.legend(['linear', 'cubic'], loc = 10)
#plt.show()



# Alternative method -> labelling each line as it is created
plt.plot([0, 1, 2, 3, 4], [0, 1, 2, 3, 4], label = "linear")
plt.plot([0, 1, 2, 3, 4], [0, 1, 4, 9, 16], label = "parabola")
plt.plot([0, 1, 2, 3, 4], [0, 1, 8, 27, 64], label = "cubic")
# .legend() command still needed
#plt.legend()
#plt.show()
