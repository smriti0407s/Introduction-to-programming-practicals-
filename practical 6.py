#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: smritisingh
"""

"""
Practical 6: Arrays - 2D arrays (lists), NumPy, Indexing and Slicing
Requires: pip install numpy
"""
import numpy as np

# =====================  2D Arrays using Lists  =====================

# ---------- Question 1: Creating and Accessing a 2D Array ----------
print("----- Question 1 -----")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Entire Matrix:")
for row in matrix:
    print(row)
print("First Row:", matrix[0])
print("Element at (2,3):", matrix[1][2])

# ---------- Question 2: Matrix Traversal ----------
print("\n----- Question 2 -----")
print("Row-wise Traversal:")
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()

print("Column-wise Traversal:")
for j in range(len(matrix[0])):
    for i in range(len(matrix)):
        print(matrix[i][j], end=" ")
    print()

# ---------- Question 3: Sum of Rows and Columns ----------
print("\n----- Question 3 -----")
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
matrix = []
print("Enter matrix elements (one row per line, space separated):")
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

print("Row Sums:")
for row in matrix:
    print(sum(row))

print("Column Sums:")
for j in range(cols):
    total = 0
    for i in range(rows):
        total += matrix[i][j]
    print(total)

# ---------- Question 4: Matrix Addition ----------
print("\n----- Question 4 -----")
rows = 2
cols = 2
A = []
B = []
print("Enter first matrix:")
for i in range(rows):
    A.append(list(map(int, input().split())))
print("Enter second matrix:")
for i in range(rows):
    B.append(list(map(int, input().split())))

result = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(A[i][j] + B[i][j])
    result.append(row)

print("Result Matrix:")
for row in result:
    print(row)

# ---------- Question 5: Transpose of a Matrix ----------
print("\n----- Question 5 -----")
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print("Original Matrix:")
for row in matrix:
    print(row)

transpose = []
for j in range(len(matrix[0])):
    row = []
    for i in range(len(matrix)):
        row.append(matrix[i][j])
    transpose.append(row)

print("Transpose Matrix:")
for row in transpose:
    print(row)

# =====================  NumPy Arrays  =====================

# ---------- Question 6: Array Creation ----------
print("\n----- Question 6 -----")
a = np.array([1, 2, 3, 4])
b = np.zeros((2, 3))
c = np.ones((3, 2))
for arr in (a, b, c):
    print(arr)
    print("Shape:", arr.shape)
    print("Data Type:", arr.dtype)

# ---------- Question 7: Array Indexing and Slicing ----------
print("\n----- Question 7 -----")
arr = np.array([[10, 20, 30],
                [40, 50, 60],
                [70, 80, 90]])
print("Specific Element:", arr[1, 2])
print("First Row:", arr[0])
print("Second Column:", arr[:, 1])
print("Sliced Array:")
print(arr[0:2, 1:3])

# ---------- Question 8: Arithmetic Operations on Arrays ----------
print("\n----- Question 8 -----")
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)

# List approach
list1 = [10, 20, 30]
list2 = [1, 2, 3]
result = []
for i in range(len(list1)):
    result.append(list1[i] + list2[i])
print("List Addition:", result)

# ---------- Question 9: Statistical Operations ----------
print("\n----- Question 9 -----")
arr = np.array([10, 20, 30, 40, 50])
print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Standard Deviation:", np.std(arr))

# ---------- Question 10: Reshaping Arrays ----------
print("\n----- Question 10 -----")
arr = np.array([1, 2, 3, 4, 5, 6])
print("Original Array:")
print(arr)
print("2D Array:")
print(arr.reshape(2, 3))
print("Reshaped Again:")
print(arr.reshape(3, 2))
# Total number of elements must stay the same while reshaping.

# ---------- Question 11: Matrix Operations ----------
print("\n----- Question 11 -----")
A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])
print("Matrix Multiplication:")
print(A @ B)
print("Transpose of A:")
print(A.T)

# Manual matrix multiplication
result = [[0, 0], [0, 0]]
for i in range(2):
    for j in range(2):
        for k in range(2):
            result[i][j] += A[i][k] * B[k][j]
print("Manual Multiplication:")
for row in result:
    print(row)

# ---------- Question 12: Real-World Dataset Analysis ----------
print("\n----- Question 12 -----")
marks = np.array([
    [85, 90, 78, 88],
    [70, 75, 80, 85],
    [95, 92, 98, 96]
])
print("Student Marks:")
print(marks)
print("Average Marks Per Student:")
print(np.mean(marks, axis=1))
print("Highest Marks:", np.max(marks))
print("Lowest Marks:", np.min(marks))
print("Average Marks Per Subject:")
print(np.mean(marks, axis=0))

# =====================  Indexing & Slicing (Part 2)  =====================
# (This part appears in your manual after Practical 7; it belongs to arrays.)

print("\n===== Indexing & Slicing =====")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Basic Indexing in 2D Array
print("First:", matrix[0][0])
print("Last:", matrix[2][2])
print("Middle:", matrix[1][1])

# Row and Column Access
print("Second Row:", matrix[1])
print("Third Column:")
for row in matrix:
    print(row[2])
# A list stores rows separately, so a loop is needed to get a full column.

# Negative Indexing
print("Last Row:", matrix[-1])
print("Last Column:")
for row in matrix:
    print(row[-1])
print("Bottom Right:", matrix[-1][-1])

# Slicing Rows
print(matrix[0:2])
print(matrix[-2:])

# Partial Slicing (top-left 2x2)
sub = [row[0:2] for row in matrix[0:2]]
print(sub)
# Lists cannot slice rows and columns together, so a comprehension is needed.

# NumPy indexing
arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
print("Element:", arr[1, 2])
print("First Row:", arr[0])
print("Second Column:", arr[:, 1])

# NumPy slicing
print(arr[0:2, :])
print(arr[:, -1])

# Submatrix extraction
arr = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])
print(arr[1:3, 1:3])