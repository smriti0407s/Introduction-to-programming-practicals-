"""
VBCS1101: Introduction to Programming
Practical 3: Decision-making using if, if-else, if-elif-else and nested conditionals
Name: Smriti Singh | Roll No: 26318A0067
"""

# ---------------------------------------------------------------
# Question 1: Basic If Condition
# ---------------------------------------------------------------
print("----- Question 1 -----")
a = int(input("Enter a number: "))
if a > 0:
    print("The number is positive")


# ---------------------------------------------------------------
# Question 2: If-Else Decision Making (even / odd)
# ---------------------------------------------------------------
print("\n----- Question 2 -----")
a = int(input("Enter a number: "))
if a % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")


# ---------------------------------------------------------------
# Question 3: Multiple Conditions using elif
# ---------------------------------------------------------------
print("\n----- Question 3 -----")
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 50:
    print("C")
else:
    print("Fail")


# ---------------------------------------------------------------
# Question 4: Nested If Statements (voting eligibility)
# ---------------------------------------------------------------
print("\n----- Question 4 -----")
age = int(input("Enter your age: "))
n = input("Enter your nationality: ")
if age >= 18:
    if n == "Indian":
        print("Eligible to vote")
    else:
        print("Not eligible to vote")
else:
    print("Not eligible to vote")


# ---------------------------------------------------------------
# Question 5: Largest of Three Numbers
# ---------------------------------------------------------------
print("\n----- Question 5 -----")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("a is greater")
elif b >= a and b >= c:
    print("b is greater")
else:
    print("c is greater")
# Using >= means equal values are handled (the first largest one is reported).


# ---------------------------------------------------------------
# Question 6: Leap Year Checker
# ---------------------------------------------------------------
print("\n----- Question 6 -----")
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")


# ---------------------------------------------------------------
# Question 7: Simple Calculator using Conditions
# ---------------------------------------------------------------
print("\n----- Question 7 -----")
a = int(input("Enter a: "))
b = int(input("Enter b: "))
op = input("Enter operator: ")

if op == '+':
    c = a + b
    print("Addition is =", c)
elif op == '-':
    c = a - b
    print("Subtraction is =", c)
elif op == '*':
    c = a * b
    print("Multiplication is =", c)
elif op == '%':
    c = a % b
    print("Mod is =", c)
elif op == '/':
    if b != 0:
        c = a / b
        print("Div is =", c)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")


# ---------------------------------------------------------------
# Question 8: Discount Eligibility System
# ---------------------------------------------------------------
print("\n----- Question 8 -----")
purchase_amount = int(input("Enter amount: "))
if purchase_amount >= 2000:
    discount = purchase_amount * 0.20
    amount = purchase_amount - discount
    print("Amount after discount", amount)
elif purchase_amount >= 1000:
    discount = purchase_amount * 0.10
    amount = purchase_amount - discount
    print("Amount after discount", amount)
else:
    print("No discount")
    print("Amount", purchase_amount)


# ---------------------------------------------------------------
# Question 9: Triangle Type Identifier
# ---------------------------------------------------------------
print("\n----- Question 9 -----")
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

if a == b and b == c:
    print("Equilateral Triangle")
elif a == b or b == c or a == c:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")


# ---------------------------------------------------------------
# Question 10: Menu-Driven Program
# ---------------------------------------------------------------
print("\n----- Question 10 -----")
print("-------- MENU --------")
print("1. Check Even/odd")
print("2. Find Largest of Three Numbers")
print("3. Grade System")
choice = int(input("Enter a choice (1-3): "))

if choice == 1:
    a = int(input("Enter a number: "))
    if a % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")
elif choice == 2:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    if a >= b and a >= c:
        print("a is greater")
    elif b >= a and b >= c:
        print("b is greater")
    else:
        print("c is greater")
elif choice == 3:
    marks = int(input("Enter your marks: "))
    if marks >= 90:
        print("Grade = A")
    elif marks >= 70:
        print("Grade = B")
    elif marks >= 50:
        print("Grade = C")
    else:
        print("Grade = Fail")
else:
    print("Invalid choice")
