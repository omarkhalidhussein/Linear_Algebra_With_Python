 ## 
# ======================================================================================================================
# Name        : EX4_Python_Program_To_RREF_Manual_Row_Operations.py
# Author      : Omar Khalid
# Created on  : July 8, 2025
# Description : Python Programming >> EX4 Python Program To PrintRREF Manual Row Operations
# ======================================================================================================================
##

import numpy as np

A = np.array([
    [0, 1, 1, -2, -3],
    [1, 2, -1, 0, 2],
    [2, 4, 1, -3, -2],
    [1, -4, -7, -1, -19]
], dtype=float)

print("Step 1: Initial Augmented Matrix:")
print(A)

# Swap row 0 and row 1
A[[0,1]]=A[[1,0]]

print("Step 2: Swap R1 and R2")
print(A)

# R3 = R3 - 2 * R1
A[2] = A[2] - 2 * A[0]

# R4 = R4 - 1 * R1
A[3] = A[3] - A[0]

print("Step 3: Eliminate below pivot in column 1")
print(A)

# R1 = -2 * R2 + R1
A[0] = -2 * A[1] + A[0]

# R4 = 6 * R2 + R4
A[3] = 6 * A[1] + A[3]

print("Step 4: Apply row operations on R1 and R4")
print(A)

# R3 = (1/3) * R3
A[2] = (1/3) * A[2]

print("Step 5: Scale row R3 by 1/3")
print(A)

# R1 = 3 * R3 + R1
A[0] = 3 * A[2] + A[0]

# R2 = -1 * R3 + R2
A[1] = -1 * A[2] + A[1]

print("Step 6: Row operations using R3")
print(A)


# R4 = (-1/13) * R4
A[3] = (-1 / 13) * A[3]

print("Step 7: Normalize R4 (make pivot = 1)")
print(A)

# R1 = -R4 + R1
A[0] = -A[3] + A[0]

# R2 = R4 + R2
A[1] = A[3] + A[1]

# R3 = R4 + R3
A[2] = A[3] + A[2]

print("Step 8: Eliminate column 4 using R4")
print(A)
