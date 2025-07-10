##
# ======================================================================================================================
# Name        : EX3_Python_Program_Solve_3x3_System_Using_Linalg.py
# Created on  : July 10, 2025
# Description : Python Programming >> EX3 Solve 3x3 System using NumPy's linalg.solve and Rank Analysis
# ======================================================================================================================
##

import numpy as np

A = np.array([
    [1, 2, 1],
    [2, 1, -1],
    [3, 3, 2]
], dtype=float)

B = np.array([6, 3, 11], dtype=float)

# ================================
#  Step 1: Solve the system
# ================================
try:
    X = np.linalg.solve(A, B)
    print("Solution using linalg.solve():")
    print("x =", X[0])
    print("y =", X[1])
    print("z =", X[2])
except np.linalg.LinAlgError as e:
    print("System has no unique solution:", e)

# ================================
#  Step 2: Verify the solution
# ================================
check = np.dot(A, X)
print("\n Check A · X = B ?")
print("A · X =", check)
print("Original B =", B)

# ================================
#  Step 3: Check system type using rank
# ================================
aug = np.column_stack((A, B))
rank_A = np.linalg.matrix_rank(A)
rank_aug = np.linalg.matrix_rank(aug)

print("\n🔍 System Type:")
if rank_A != rank_aug:
    print("Inconsistent system (No solution)")
elif rank_A < A.shape[1]:
    print("Infinitely many solutions")
else:
    print("Unique solution")
