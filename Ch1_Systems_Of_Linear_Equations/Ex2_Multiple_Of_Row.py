##
# ======================================================================================================================
# Name        : EX2_Python_Program_To_Multiple_Of_Row.py
# Author      : Omar Khalid
# Created on  : July 7, 2025
# Description : Python Programming >> EX1 Python Program To Multiple Of Row
# ======================================================================================================================
##

def add_multiple_of_row(matrix, source_row, target_row, factor):
    matrix[target_row] += factor * matrix[source_row]



M = np.array([[1, 2], [3, 4]])
add_multiple_of_row(M, 0, 1, -3)
print(M)
