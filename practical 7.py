#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: smritisingh
"""

"""
Practical 7: Lists and Tuples - Creation, Indexing, and Methods
"""

# ---------- Question 1: Creating Lists and Tuples ----------
print("----- Question 1 -----")
numbers = [10, 20, 30, 40]
fruits = ("Apple", "Banana", "Mango")
print(numbers)
print(fruits)
print(type(numbers))
print(type(fruits))
# List uses [], tuple uses ()

# ---------- Question 2: Indexing ----------
print("\n----- Question 2 -----")
numbers = [10, 20, 30, 40, 50]
items = ("A", "B", "C", "D", "E")
print("First:", numbers[0], items[0])
print("Last:", numbers[-1], items[-1])
print("Middle:", numbers[2], items[2])

# ---------- Question 3: Slicing ----------
print("\n----- Question 3 -----")
print(numbers[:3])
print(numbers[-2:])
print(numbers[::2])
print(items[:3])
print(items[-2:])
print(items[::2])

# ---------- Question 4: Mutability vs Immutability ----------
print("\n----- Question 4 -----")
numbers = [10, 20, 30]
numbers[1] = 50
print(numbers)

items = ("A", "B", "C")
try:
    items[1] = "X"
except TypeError as e:
    print("Error:", e)
# Lists are mutable (can be changed); tuples are immutable.

# ---------- Question 5: Adding Elements ----------
print("\n----- Question 5 -----")
numbers = [10, 20, 30]
numbers.append(40)
numbers.insert(1, 15)
print(numbers)

# ---------- Question 6: Removing Elements ----------
print("\n----- Question 6 -----")
numbers = [10, 20, 30, 40]
numbers.remove(20)
print(numbers)
numbers.pop()
print(numbers)
try:
    numbers.remove(100)
except ValueError as e:
    print("Error:", e)

# ---------- Question 7: sort() and reverse() ----------
print("\n----- Question 7 -----")
numbers = [40, 10, 30, 20]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)
numbers.reverse()
print(numbers)

# ---------- Question 8: Tuple Methods ----------
print("\n----- Question 8 -----")
t = (10, 20, 30, 20, 40)
print("Count:", t.count(20))
print("Index:", t.index(30))
try:
    print(t.index(100))
except ValueError as e:
    print("Error:", e)

# ---------- Question 9: Nested Lists ----------
print("\n----- Question 9 -----")
matrix = [
    [1, 2],
    [3, 4]
]
print(matrix[0][1])
matrix[1][0] = 10
print(matrix)

# ---------- Question 10: List <-> Tuple ----------
print("\n----- Question 10 -----")
numbers = [10, 20, 30]
t = tuple(numbers)
print(t)
l = list(t)
l.append(40)
print(l)

# ---------- Question 11: Iteration ----------
print("\n----- Question 11 -----")
numbers = [10, 20, 30, 40]
items = ("A", "B", "C")
total = 0
for n in numbers:
    print(n)
    total += n
print("Sum =", total)
for item in items:
    print(item)

# ---------- Question 12: Shopping Cart System ----------
print("\n----- Question 12 -----")
cart = ["Milk", "Bread", "Eggs"]
categories = ("Food", "Drinks", "Snacks")
cart.append("Butter")
cart.remove("Bread")
print("Categories:", categories)
print("Shopping Cart:", cart)
print("Total Items:", len(cart))