import numpy as np

# 1) np.array
arr_from_list = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print("np.array result:")
print(arr_from_list)
print("size:", np.size(arr_from_list))
print("shape:", np.shape(arr_from_list))
print("dimension:", np.ndim(arr_from_list), "D Array\n")

# 2) np.zeros
zeros_arr = np.zeros((3, 4))
print("np.zeros result:")
print(zeros_arr)
print("size:", np.size(zeros_arr))
print("shape:", np.shape(zeros_arr))
print("dimension:", np.ndim(zeros_arr), "D Array\n")

# 3) np.ones
ones_arr = np.ones((2, 5))
print("np.ones result:")
print(ones_arr)
print("size:", np.size(ones_arr))
print("shape:", np.shape(ones_arr))
print("dimension:", np.ndim(ones_arr), "D Array\n")

# 4) np.diag
# Creates a square matrix with diagonal values from the list
diag_arr = np.diag([10, 20, 30, 40])
print("np.diag result:")
print(diag_arr)
print("size:", np.size(diag_arr))
print("shape:", np.shape(diag_arr))
print("dimension:", np.ndim(diag_arr), "D Array\n")

# 5) np.arange
arange_arr = np.arange(0, 20, 2)
print("np.arange result:")
print(arange_arr)
print("size:", np.size(arange_arr))
print("shape:", np.shape(arange_arr))
print("dimension:", np.ndim(arange_arr), "D Array\n")

# 6) np.linspace
linspace_arr = np.linspace(0, 1, 6)
print("np.linspace result:")
print(linspace_arr)
print("size:", np.size(linspace_arr))
print("shape:", np.shape(linspace_arr))
print("dimension:", np.ndim(linspace_arr), "D Array\n")

# 7) np.logspace
logspace_arr = np.logspace(1, 3, 5)
print("np.logspace result:")
print(logspace_arr)
print("size:", np.size(logspace_arr))
print("shape:", np.shape(logspace_arr))
print("dimension:", np.ndim(logspace_arr), "D Array\n")

# -------------------------------------------------
# Input-based array (after all pre-made arrays)
# -------------------------------------------------
print("Create your own NumPy array using input.")
print("Type numbers with spaces. Example: 5 10 15 20")
user_raw = input("Enter numbers: ")

# Easy version: split by space, then convert to int
user_numbers = user_raw.split()
user_array = np.array(user_numbers, dtype=int)

print("Your input array:")
print(user_array)
print("size:", np.size(user_array))
print("shape:", np.shape(user_array))
print("dimension:", np.ndim(user_array), "D Array\n")

# Variation 2: comma-separated input
print("Variation 2: Type numbers with commas. Example: 5,10,15,20")
user_raw_comma = input("Enter comma numbers: ")
comma_list = user_raw_comma.split(",")
comma_array = np.array(comma_list, dtype=int)

print("Your comma array:")
print(comma_array)
print("size:", np.size(comma_array))
print("shape:", np.shape(comma_array))
print("dimension:", np.ndim(comma_array), "D Array\n")

# Variation 3: loop input (Enter Input 1, Enter Input 2, ...)
print("Variation 3: Loop input one value at a time")
count = int(input("How many inputs? "))
loop_values = []

for i in range(count):
    value = int(input("Enter Input " + str(i + 1) + ": "))
    loop_values.append(value)

loop_array = np.array(loop_values)

print("Your loop array:")
print(loop_array)
print("size:", np.size(loop_array))
print("shape:", np.shape(loop_array))
print("dimension:", np.ndim(loop_array), "D Array\n")

# -------------------------------------------------
# Basic operations demonstration
# -------------------------------------------------
array1 = np.array([1, 2, 3])
array2 = np.array([5, 3, 3])

print("Operations Demo:")
print("array1:", array1)
print("array2:", array2)
print("array1 + array2 =", array1 + array2)
print("array1 - array2 =", array1 - array2)
print("array1 * array2 =", array1 * array2)
print("array1 / array2 =", array1 / array2)
