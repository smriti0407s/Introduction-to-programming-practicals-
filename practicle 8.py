#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: smritisingh
"""

"""
Practical 8: Dictionaries - Creation, Indexing, and Methods
"""

# ---------- Question 1: Creating a Dictionary ----------
print("----- Question 1 -----")
student = {
    "Name": "Rahul",
    "Age": 20,
    "Marks": 85
}
print(student)
print(type(student))
# A dictionary stores key-value pairs; each key is unique.

# ---------- Question 2: Accessing Values ----------
print("\n----- Question 2 -----")
print(student["Name"])
print(student["Marks"])
try:
    print(student["City"])
except KeyError as e:
    print("KeyError: key not found ->", e)

# ---------- Question 3: get() ----------
print("\n----- Question 3 -----")
print(student.get("Name"))
print(student.get("City"))                    # None
print(student.get("City", "Not Available"))   # default value

# ---------- Question 4: Adding and Updating ----------
print("\n----- Question 4 -----")
student = {"Name": "Rahul", "Age": 20}
student["Marks"] = 85    # Add
student["Age"] = 21      # Update
print(student)

# ---------- Question 5: Removing Elements ----------
print("\n----- Question 5 -----")
student = {"Name": "Rahul", "Age": 20, "Marks": 85}
student.pop("Marks")
print(student)
del student["Age"]
print(student)
try:
    student.pop("City")
except KeyError as e:
    print("KeyError: key not found ->", e)

# ---------- Question 6: Iterating ----------
print("\n----- Question 6 -----")
student = {"Name": "Rahul", "Age": 20, "Marks": 85}
print("Keys:")
for key in student:
    print(key)
print("Values:")
for value in student.values():
    print(value)
print("Key-Value Pairs:")
for key, value in student.items():
    print(key, ":", value)

# ---------- Question 7: keys(), values(), items() ----------
print("\n----- Question 7 -----")
keys = list(student.keys())
values = list(student.values())
items = list(student.items())
print(keys)
print(values)
print(items)

# ---------- Question 8: Frequency Counting ----------
print("\n----- Question 8 -----")
text = input("Enter a string: ")
frequency = {}
for ch in text:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1
print(frequency)

# ---------- Question 9: Nested Dictionary ----------
print("\n----- Question 9 -----")
students = {
    "101": {"Name": "Rahul", "Marks": 85},
    "102": {"Name": "Priya", "Marks": 92}
}
print(students["101"]["Name"])
students["102"]["Marks"] = 95
print(students)

# ---------- Question 10: Dictionary Merging ----------
print("\n----- Question 10 -----")
dict1 = {"A": 10, "B": 20}
dict2 = {"B": 50, "C": 30}
dict1.update(dict2)
print(dict1)
# Same key: the value from the second dictionary overwrites the first.

# ---------- Question 11: Sorting ----------
print("\n----- Question 11 -----")
student = {"Rahul": 85, "Priya": 92, "Amit": 78}
print("Sorted by Keys:")
for key in sorted(student):
    print(key, student[key])

print("\nSorted by Values:")
for key, value in sorted(student.items(), key=lambda x: x[1]):
    print(key, value)

# ---------- Question 12: Inventory System ----------
print("\n----- Question 12 -----")
inventory = {"Laptop": 10, "Mouse": 25, "Keyboard": 15}
inventory["Monitor"] = 8       # Add product
inventory["Mouse"] = 30        # Update stock
inventory.pop("Keyboard")      # Remove product

print("Final Inventory:")
for product, quantity in inventory.items():
    print(product, ":", quantity)