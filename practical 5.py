#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: smritisingh
"""

"""
Practical 5: Loop Control Statements (break, continue, pass)
"""

# ---------- Question 1: break ----------
print("----- Question 1 -----")
for i in range(1, 11):
    if i == 5:
        break
    print(i)

# ---------- Question 2: continue ----------
print("\n----- Question 2 -----")
for i in range(1, 11):
    if i % 3 == 0:
        continue
    print(i)

# ---------- Question 3: break vs continue ----------
print("\n----- Question 3 -----")
print("Using break:")
for i in range(1, 11):
    if i == 5:
        break
    print(i)

print("Using continue:")
for i in range(1, 11):
    if i == 5:
        continue
    print(i)
# break ends the loop completely; continue skips only the current iteration.

# ---------- Question 4: Searching in a List ----------
print("\n----- Question 4 -----")
numbers = [10, 20, 30, 40, 50, 60]
search = int(input("Enter number to search: "))

for i in range(len(numbers)):
    if numbers[i] == search:
        print("Element found at position", i)
        break
else:
    print("Element not found")

# ---------- Question 5: First Divisible Number ----------
print("\n----- Question 5 -----")
n = int(input("Enter a number: "))
for i in range(1, 101):
    if i % n == 0:
        print("First divisible number is:", i)
        break

# ---------- Question 6: Skip Negative Numbers ----------
print("\n----- Question 6 -----")
numbers = [10, -5, 20, -8, 15, -2, 30]
for num in numbers:
    if num < 0:
        continue
    print(num)

# ---------- Question 7: Sum of Valid Inputs Only ----------
print("\n----- Question 7 -----")
total = 0
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    if num < 0:
        continue
    total += num
print("Sum =", total)

# ---------- Question 8: Password Retry System ----------
print("\n----- Question 8 -----")
password = "python123"

for attempt in range(3):
    user = input("Enter password: ")
    if user == password:
        print("Access Granted")
        break
else:
    # runs only if the loop finished without break (3 wrong attempts)
    print("Access Denied! 3 attempts finished.")

# ---------- Question 9: pass ----------
print("\n----- Question 9 -----")
for i in range(1, 6):
    if i == 3:
        pass          # placeholder: an empty block would be a syntax error
    else:
        print(i)

# ---------- Question 10: Pattern with Conditional Skipping ----------
print("\n----- Question 10 -----")
for i in range(1, 6):
    for j in range(1, 6):
        if j % 2 == 0:
            continue
        print(j, end=" ")
    print()