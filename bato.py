import numpy as np

five_by_seven = np.array(([
    [1123,2,3,4,5,36,36],
    [3,443,5,5,6,34,39],
    [1,421,7,92,6,77,89],
    [5,623,4,32,3,66,77],
    [7,6666,9,32,3,33,44]
]))

six_by_six = np.array([
    [1,2,3,4,5,6],
    [7,8,9,0,9,8],
    [7,6,5,4,3,2],
    [3,4,5,6,7,8],
    [1,0,1,2,3,4],
    [5,6,7,8,9,0]
])


four_by_four = np.zeros((4,4))

five_by_seven_size = np.size(five_by_seven)
five_by_seven_shape = np.shape(five_by_seven)
five_by_seven_dim = np.ndim(five_by_seven)

print(five_by_seven)
print("5x7 size: " + str(five_by_seven_size))
print("5x7 shape: " + str(five_by_seven_shape))
print("5x7 dimension: " + str(five_by_seven_dim) + "D Array\n")

six_by_six_size = np.size(six_by_six)
six_by_six_shape = np.shape(six_by_six)
six_by_six_dim = np.ndim(six_by_six)

print(six_by_six)
print("6x6 size: " + str(six_by_six_size))
print("6x6 shape: " + str(six_by_six_shape))
print("6x6 dimension: " + str(six_by_six_dim) + "D Array\n")


size = np.size(four_by_four)
shape = np.shape(four_by_four)
dim = np.ndim(four_by_four)

print(four_by_four)
print("4x4 size: " + str(size))
print("4x4 shape: " + str(shape))
print("4x4 dimension: " + str(dim) + "D Array")