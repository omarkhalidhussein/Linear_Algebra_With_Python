
##
# ======================================================================================================================
# Name        : EX1_Python_Program_To_Print_Augmented_Matrix.py
# Author      : Omar Khalid
# Created on  : July 7, 2025
# Description : Python Programming >> EX1 Python Program To Print Augmented Matrix 
# ======================================================================================================================
##

import numpy as np

# Example: The following system of equations
# 2x + 3y = 5
# 4x -  y = 6

A = np.array([[2, 3], [4, -1]])  # Coefficient matrix
B = np.array([[5], [6]])         # Constant terms (right-hand side)

# Augmented matrix
augmented_matrix = np.hstack((A, B))

print("Coefficient Matrix A:\n", A)
print("\nConstant Terms Matrix B:\n", B)
print("\nAugmented Matrix:\n", augmented_matrix)
