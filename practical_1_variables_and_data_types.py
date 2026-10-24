"""
VBCS1101: Introduction to Programming
Practical 1: Basics of Python - Variables, Constants, and Data Types
Name: Smriti Singh | Class: FYCS | Roll No: 26318A0067 | Division: A
"""

# ---------------------------------------------------------------
# Question 1: Variable Creation and Naming Rules
# ---------------------------------------------------------------
print("----- Question 1 -----")
name = "Smriti"
print("Name is:", name)
age = 18
print("Age is:", age)
marks = "10/10"
print("Marks is:", marks)
city = "Mumbai"
print("City is:", city)

# Invalid variable names (uncomment to observe the errors):
# 1name = "Smriti"    # SyntaxError: a name cannot start with a digit
# class = "FYCS"      # SyntaxError: 'class' is a reserved keyword
# my-name = "Smriti"  # SyntaxError: '-' is treated as the minus operator
#
# Corrected versions:
name1 = "Smriti"      # starts with a letter
class_name = "FYCS"   # not a keyword
my_name = "Smriti"    # underscore instead of hyphen


# ---------------------------------------------------------------
# Question 2: Dynamic Typing in Python
# ---------------------------------------------------------------
print("\n----- Question 2 -----")
a = 10
print("a =", a)
print("type of a is =", type(a))

print("after reassign to string")
a = "Smriti"
print("a =", a)
print("type of a is =", type(a))

print("after reassign to float")
a = 10.5
print("a =", a)
print("type of a is =", type(a))

# Python vs statically typed languages:
# In Python (dynamically typed) the type belongs to the value, not the
# variable, so the same name can hold an int, then a str, then a float.
# In statically typed languages (C, C++, Java) the type is declared up
# front and is fixed; assigning a different type causes a compile error.


# ---------------------------------------------------------------
# Question 3: Constants Simulation
# ---------------------------------------------------------------
print("\n----- Question 3 -----")
PI = 3.14159
GRAVITY = 9.8
MAX_USERS = 100
print("PI =", PI)
print("Gravity =", GRAVITY)
print("MAX_USERS =", MAX_USERS)

# Python does not enforce constants: PI = 3 would work without any error.
# By convention, names written in UPPER_CASE signal "do not change this".
# Python trusts programmers ("we are all consenting adults").


# ---------------------------------------------------------------
# Question 4: Data Type Identification System
# ---------------------------------------------------------------
print("\n----- Question 4 -----")
a = int(input("Enter an integer: "))
print("The value of a =", a, "type of a =", type(a))

b = float(input("Enter float: "))
print("The value of b =", b, "type of b =", type(b))

c = input("Enter string: ")
print("The value of c =", c, "type of c =", type(c))

d = True
print("The value of d =", d, "type of d =", type(d))

# Summary table of values vs types
print("\n{:<10}{:<15}".format("Value", "Type"))
for value in (a, b, c, d):
    print("{:<10}{:<15}".format(str(value), type(value).__name__))


# ---------------------------------------------------------------
# Question 5: Type Conversion (Casting)
# ---------------------------------------------------------------
print("\n----- Question 5 -----")
age = input("Enter Age: ")
marks = input("Enter Marks: ")

print("Without conversion")
print(age + marks)          # strings get concatenated: "10" + "10" -> "1010"

age = int(age)
marks = float(marks)
print("age after 5 years:", age + 5)
print("marks + 2:", marks + 2)

# Without conversion, age + 5 raises:
# TypeError: can only concatenate str (not "int") to str


# ---------------------------------------------------------------
# Question 6: Implicit vs Explicit Type Conversion
# ---------------------------------------------------------------
print("\n----- Question 6 -----")
a = 10
b = 5.5
print(a + b)                # implicit: int is promoted to float -> 15.5

c = "5"
# print(a + c)              # TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(a + int(c))           # explicit casting fixes it -> 15

# Implicit rule: Python automatically converts the "smaller" type to the
# "larger" one (bool -> int -> float -> complex) to avoid losing data.


# ---------------------------------------------------------------
# Question 7: Memory Behavior of Variables
# ---------------------------------------------------------------
print("\n----- Question 7 -----")
a = 100
b = 100
print(id(a))
print(id(b))                # same id: both names refer to the same object

b = 200                     # modify one variable
print(id(a), id(b))         # b now points to a different object

# Immutability: int, float, str, tuple are immutable - changing the value
# creates a new object. Mutable types (list, dict, set) can change in place.


# ---------------------------------------------------------------
# Question 8: Swapping Variables Using Multiple Methods
# ---------------------------------------------------------------
print("\n----- Question 8 -----")
# a) Third variable
a = 10
b = 20
temp = a
a = b
b = temp
print(a, b)

# b) Tuple unpacking
a = 10
b = 20
a, b = b, a
print(a, b)

# Comparison: the third-variable method uses extra memory and 3 lines;
# tuple unpacking is shorter and more "Pythonic".


# ---------------------------------------------------------------
# Question 9: Data Type-Based Calculator
# ---------------------------------------------------------------
print("\n----- Question 9 -----")
first = input("Enter first value: ")
second = input("Enter second value: ")

try:
    num1 = float(first)
    num2 = float(second)
    print("Addition =", num1 + num2)
except ValueError:
    if first.isalpha() and second.isalpha():
        print("Concatenation =", first + second)
    else:
        print("Invalid input")


# ---------------------------------------------------------------
# Question 10: Boolean Logic and Data Types
# ---------------------------------------------------------------
print("\n----- Question 10 -----")
age = int(input("Enter age: "))
marks = int(input("Enter marks: "))

isAdult = age > 18
isPassed = marks > 50

print("Adult:", isAdult)
print("Passed:", isPassed)

if isAdult and isPassed:
    print("Eligible")
else:
    print("Not eligible")


# ---------------------------------------------------------------
# Question 11: Real-World Scenario - Temperature Converter
# ---------------------------------------------------------------
print("\n----- Question 11 -----")
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
print(f"{celsius:.2f}C = {fahrenheit:.2f}F")
