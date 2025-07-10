##
# ======================================================================================================================
# Name        : EX2_Python_Program_To_Print_RREF(2)_Manual_Row_Operations.py
# Created on  : July 10, 2025
# Description : Python Programming >> EX1 Python Program To Print RREF(2) Manual Row Operations
# ======================================================================================================================
##


import numpy as np

A = np.array([
    [1,  1,  2,  -5,   3],    # R1
    [2,  5, -1,  -9,  -3],    # R2
    [2,  1, -1,   3, -11],    # R3
    [1, -3,  2,   7,  -5]     # R4
], dtype=float)

# R2 = -2 * R1 + R2
A[1] = -2 * A[0] + A[1]

# R3 = -2 * R1 + R3
A[2] = -2 * A[0] + A[2]

# R4 = -1 * R1 + R4
A[3] = -1 * A[0] + A[3]

print("Step 1: Make all values below pivot in column 1++++ = 0")
print(A)

# Swap R2 with R3
A[[1,2]] = A[[2,1]]

print("Step 2: Swap R2 with R3")
print(A)

# R2 = -1 * R2
A[1] = -1 * A[1]

print("Step 3: Multiply R2 by -1")
print(A)

# R1 = -1 * R2 + R1
A[0] = -1 * A[1] + A[0]

# R3 = -3 * R2 + R3
A[2] = -3 * A[1] + A[2]

# R4 = 4 * R2 + R4
A[3] = 4 * A[1] + A[3]

print("Step 4: Apply row operations using R2")
print(A)

# R3 = (-1/20) * R3
A[2] *= -1/20

print("Step 5: Scale R3 so pivot becomes 1")
print(A)

# R1 = 3 * R3 + R1
A[0] = 3 * A[2] + A[0]

# R2 = -5 * R3 + R2
A[1] = -5 * A[2] + A[1]

# R4 = -20 * R3 + R4
A[3] = -20 * A[2] + A[3]

print("Step 6=: Zero out column 3 using R3")
print(A)  

# ======================================================
#  System Type and Conclusion:
#
# After applying row operations and reducing the augmented matrix
# to Row Echelon Form, we observed that the last row contains only zeros.
#
# This indicates that the rank of the matrix is 3,
# while the number of variables is 4.
#
# Since:
#     Rank(A) = Rank([A|B]) < Number of variables
#
#  Conclusion:
# → The system has infinitely many solutions.
# → There is one free variable (w = t), and all other variables are expressed in terms of t.
# ======================================================
