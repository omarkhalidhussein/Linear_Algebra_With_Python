##
# ======================================================================================================================
# Name        : EX2_Python_Program To Swap_Rows_using_Numpy.py
# Author      : Omar Khalid
# Created on  : July 8, 2025
# Description : Python Programming >> EX2 Python Program To Swap Rows using Numpy
# ======================================================================================================================
##



import numpy as np

def Swap(m, r, c):
    m[[r, c]] = m[[c, r]]
    return m

# Sample 2D array
arr = np.array([
    [1, 2, 6],
    [2, 4, 5]
])

# Swap row 0 and row 1
result = Swap(arr, 0, 1)

# Display the result
print("Array after swapping rows 0 and 1:")
print(result)
