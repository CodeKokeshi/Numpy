import numpy as np

# This is the most basic way to input 1D arrays
'''vals = []

for i in range (5):
    x = int(input(f"enter value {i+1}: "))
    vals.append(x)

arr1 = np.array(vals)

print(arr1)'''

# This is the most basic way to input in np.diag
'''vals = []

for i in range (5):
    x = int(input(f"enter value {i+1}: "))
    vals.append(x)

arr1 = np.diag(vals)

print(arr1)'''

# This is how to input 2D Arrays
'''vals = []

for r in range (2):
    row = []
    for c in range(2):
        x = int(input(f"enter value rows{r+1} cols{c+1}: "))
        row.append(x)
    vals.append(row)

arr1 = np.array(vals)

print(arr1)'''

# np.zeros dimensions
'''a = np.zeros((5,4,3)) #Five 3x4s (3D Array)
b = np.zeros((5,4)) #5x4 (2D Array)
c = np.zeros((3)) #1D Array 3 Elements
'''

