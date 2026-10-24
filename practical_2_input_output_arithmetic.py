"""
VBCS1101: Introduction to Programming
Practical 2: Input/output operations and arithmetic expressions in Python
Name: Smriti Singh | Class: FYCS (AI & ML) | Roll No: 26318A0067 | Division: A
"""

# ---------------------------------------------------------------
# Question 1: Input and output (simple print vs f-string)
# ---------------------------------------------------------------
print("----- Question 1 -----")
name = input("Enter your name: ")
age = input("Enter your age: ")

# Simple print
print("Simple print")
print("name:", name)
print("age:", age)

# Formatted string
print(f"Name: {name}, age = {age}")


# ---------------------------------------------------------------
# Question 2: Numeric Input Handling
# ---------------------------------------------------------------
print("\n----- Question 2 -----")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Addition =", num1 + num2)
print("Subtraction =", num1 - num2)
print("Multiplication =", num1 * num2)
print("Division =", num1 / num2)
# Without float()/int(), input() returns strings, so "10" + "5" -> "105".


# ---------------------------------------------------------------
# Question 3: Expression Evaluation
# ---------------------------------------------------------------
print("\n----- Question 3 -----")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

sum_val = a + b + c
avg = sum_val / 3
expression = (a + b) * c / 2

print("Sum =", sum_val)
print("Average =", avg)
print("Expression =", expression)


# ---------------------------------------------------------------
# Question 4: Operator Precedence Analysis
# ---------------------------------------------------------------
print("\n----- Question 4 -----")
print(10 + 5 * 2)        # 20   (multiplication before addition)
print((10 + 5) * 2)      # 30   (brackets first)
print(100 / 5 + 3 * 2)   # 26.0 (/ and * first, then +)


# ---------------------------------------------------------------
# Question 5: Salary Breakdown
# ---------------------------------------------------------------
print("\n----- Question 5 -----")
basic_sal = float(input("Enter your salary: "))
hra = basic_sal * 0.20
da = basic_sal * 0.10
net_sal = basic_sal + hra + da

print("Basic Salary =", basic_sal)
print("HRA =", hra)
print("DA =", da)
print("Net Salary =", net_sal)


# ---------------------------------------------------------------
# Question 6: Area and Perimeter Calculator
# ---------------------------------------------------------------
print("\n----- Question 6 -----")
PI = 3.14
length = float(input("Enter length of rectangle: "))
breadth = float(input("Enter breadth of rectangle: "))
radius = float(input("Enter radius of circle: "))

area_rect = length * breadth
peri_rect = 2 * (length + breadth)
area_circle = PI * radius * radius
circumference = 2 * PI * radius

print("Area of rectangle =", area_rect)
print("Perimeter =", peri_rect)
print("Area of circle =", area_circle)
print("Circumference =", circumference)


# ---------------------------------------------------------------
# Question 7: Unit Conversion Tool
# ---------------------------------------------------------------
print("\n----- Question 7 -----")
USD_RATE = 95.5   # fixed rate: rupees per dollar (change as needed)

km = float(input("Enter km: "))
celsius = float(input("Enter temperature in celsius: "))
rupees = float(input("Enter the rupees: "))

meters = km * 1000
fahrenheit = (celsius * 9 / 5) + 32
dollars = rupees / USD_RATE

print("Distance in meters =", meters)
print("Temperature in Fahrenheit =", fahrenheit)
print("Dollars =", dollars)


# ---------------------------------------------------------------
# Question 8: Multi-Input Single-Line Processing
# ---------------------------------------------------------------
print("\n----- Question 8 -----")
a, b, c = map(int, input("Enter three numbers separated by space: ").split())
print("Sum =", a + b + c)
print("Product =", a * b * c)


# ---------------------------------------------------------------
# Question 9: Expression-Based Grading System
# ---------------------------------------------------------------
print("\n----- Question 9 -----")
sub1 = float(input("Enter marks for Subject 1: "))
sub2 = float(input("Enter marks for Subject 2: "))
sub3 = float(input("Enter marks for Subject 3: "))

total = sub1 + sub2 + sub3
percentage = (total / 300) * 100

if percentage >= 90:
    print("Grade = 'A'")
elif percentage >= 80:
    print("Grade = 'B'")
elif percentage >= 70:
    print("Grade = 'C'")
elif percentage >= 50:
    print("Grade = 'D'")
else:
    print("Grade = 'Fail'")


# ---------------------------------------------------------------
# Question 10: Error Analysis in Expressions
# ---------------------------------------------------------------
print("\n----- Question 10 -----")
message = "Smriti " + "Singh"
print(message)

# Errors to observe (uncomment one at a time):
# print(10 / 0)            # ZeroDivisionError: division by zero
# print("Age: " + 18)      # TypeError: can only concatenate str (not "int") to str

# Handling / preventing the errors:
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero")

print("Age: " + str(18))   # convert number to string first
