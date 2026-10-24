"""
VBCS1101: Introduction to Programming
Practical 4: Looping statements (for, while, nested loops)
Name: Smriti Singh | Roll No: 26318A0067
"""

# ---------------------------------------------------------------
# Question 1: for loop syntax and range
# ---------------------------------------------------------------
print("----- Question 1 -----")
print("Numbers from 1 to 10:")
for i in range(1, 11):
    print(i)

# Print only even numbers from 1 to 10
print("\nEven numbers from 1 to 10:")
for i in range(2, 11, 2):
    print(i)

# range(start, stop, step): starts at 'start', stops BEFORE 'stop',
# and increases by 'step' each time (defaults: start=0, step=1).


# ---------------------------------------------------------------
# Question 2: while loop fundamentals
# ---------------------------------------------------------------
print("\n----- Question 2 -----")
i = 1
while i <= 10:
    print(i)
    i = i + 1

# Comparison: 'for' is best when the number of repetitions is known;
# 'while' is best when looping depends on a condition.


# ---------------------------------------------------------------
# Question 3: Sum and average using loop
# ---------------------------------------------------------------
print("\n----- Question 3 -----")
n = int(input("Enter how many numbers: "))
sum = 0
for i in range(n):
    num = int(input("Enter a number: "))
    sum = sum + num

average = sum / n
print("Sum =", sum)
print("Average =", average)


# ---------------------------------------------------------------
# Question 4: Factorial calculation (for loop and while loop)
# ---------------------------------------------------------------
print("\n----- Question 4 -----")
n = int(input("Enter a number: "))

# Using for loop
fact = 1
for i in range(1, n + 1):
    fact = fact * i
print("factorial of given number is:", fact)

# Using while loop
fact = 1
i = 1
while i <= n:
    fact = fact * i
    i = i + 1
print("factorial (while loop) is:", fact)


# ---------------------------------------------------------------
# Question 5: Multiplication table generator
# ---------------------------------------------------------------
print("\n----- Question 5 -----")
n = int(input("Enter a number: "))
print("multiplication table of =", n)
for i in range(1, 11):
    print(n, "x", i, "=", i * n)


# ---------------------------------------------------------------
# Question 6: Number reversal and palindrome check
# ---------------------------------------------------------------
print("\n----- Question 6 -----")
num = int(input("Enter a number: "))
original = num
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reversed Number =", reverse)

if original == reverse:
    print(original, "is a palindrome")
else:
    print(original, "is not a palindrome")
