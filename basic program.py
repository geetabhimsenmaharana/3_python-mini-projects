# ============================================================
# PYTHON WEEK 1 - BEGINNER BASICS
# ============================================================


# ============================================================
# 1. PRINT()
# ============================================================

# print() displays information on the screen.

print("Hello, Python!")
print("My name is G")


# ============================================================
# 2. COMMENTS
# ============================================================

# This is a single-line comment.
# Python ignores comments when running the program.

print("Comments help us explain our code.")
print("Use # in front of the line to comment the entire line.")
"""
This is a
multi-line comment.
It can be used for longer explanations.
"""


# ============================================================
# 3. VARIABLES
# ============================================================

# A variable stores a value.

name = "Geeta"
age = 30
salary = 75000

print(name)
print(age)
print(salary)

# We can change the value of a variable.

age = 31

print(age)


# ============================================================
# 4. DATA TYPES
# ============================================================

# Python has different types of data.

name = "Geeta"       # str - text
age = 30             # int - whole number
salary = 75000.50    # float - decimal number
is_student = True    # bool - True or False

# type() tells us the data type.

print(type(name))
print(type(age))
print(type(salary))
print(type(is_student))


# ============================================================
# 5. TYPE CONVERSION
# ============================================================

# Sometimes we need to convert one data type into another.

age = "30"

print(type(age))     # str

age = int(age)

print(type(age))     # int
print(age)

# Other common conversions:

number = 100

text_number = str(number)      # int → str
decimal_number = float(number) # int → float

print(text_number)
print(decimal_number)


# ============================================================
# 6. ARITHMETIC OPERATORS
# ============================================================

# Python can perform mathematical calculations.

a = 10
b = 3

print(a + b)    # Addition
print(a - b)    # Subtraction
print(a * b)    # Multiplication
print(a / b)    # Division
print(a // b)   # Floor division
print(a % b)    # Remainder
print(a ** b)   # Power


# ============================================================
# 7. COMPARISON OPERATORS
# ============================================================

# Comparison operators compare two values.
# The result is always True or False.

age = 25

print(age == 25)    # Equal to
print(age != 25)    # Not equal to
print(age > 18)     # Greater than
print(age < 18)     # Less than
print(age >= 25)    # Greater than or equal to
print(age <= 25)    # Less than or equal to


# ============================================================
# 8. INPUT()
# ============================================================

# input() allows the user to enter information.

name = input("What is your name? ")

print(f"Hello, {name}!")

# IMPORTANT:
# input() always gives us a STRING.

age = input("What is your age? ")

print(type(age))


# ============================================================
# 9. INPUT + TYPE CONVERSION
# ============================================================

# If we want to perform calculations with user input,
# we usually need to convert it.

age = int(input("Enter your age: "))

print(f"You are {age} years old.")

# Example with salary:

salary = float(input("Enter your salary: "))

print(f"Your salary is ${salary:,.2f}")


# ============================================================
# 10. STRINGS
# ============================================================

# A string is text.

first_name = "Geeta"
last_name = "Maharana"

# Combine strings.

full_name = first_name + " " + last_name

print(full_name)

# f-strings are a cleaner way to combine values and text.

print(f"My name is {first_name} {last_name}.")


# ============================================================
# 11. STRING INDEXING AND SLICING
# ============================================================

word = "Python"

# Indexing starts at 0.

print(word[0])     # P
print(word[1])     # y
print(word[2])     # t

# Negative indexing starts from the end.

print(word[-1])    # n
print(word[-2])    # o

# Slicing
# [start:stop]
# The stop position is NOT included.

print(word[0:3])   # Pyt
print(word[2:5])   # tho

# Reverse a string.

print(word[::-1])  # nohtyP


# ============================================================
# 12. STRING METHODS
# ============================================================

text = "  Hello Python  "

print(text.upper())       # Convert to uppercase
print(text.lower())       # Convert to lowercase
print(text.strip())       # Remove spaces from beginning/end

message = "I am learning Python 999 timrdf-77 on "
print("before replacing: ",message)
print(message.replace("Python", "AI"))
print("after replacing: ",message)
print(message.startswith("I"))
print(message.endswith("Python"))

# split() breaks a string into a list.
print("before split: ",message)

words = message.split()

print(words)


# ============================================================
# 13. IF / ELIF / ELSE
# ============================================================

age = 25

if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a child.")


# ============================================================
# 14. NESTED CONDITIONS + LOGICAL OPERATORS
# ============================================================

age = 25
has_id = True

# AND means both conditions must be True.

if age >= 18 and has_id:
    print("You can enter.")

# OR means at least one condition must be True.

is_weekend = True
is_holiday = False

if is_weekend or is_holiday:
    print("You don't have to work.")

# NOT reverses True/False.

is_logged_in = False

if not is_logged_in:
    print("Please log in.")


# Nested if means an if statement inside another if statement.

age = 25
has_ticket = True

if age >= 18:

    if has_ticket:
        print("You can enter the event.")
    else:
        print("You need a ticket.")

else:
    print("You must be 18 or older.")


# ============================================================
# WEEK 1 COMPLETE
# ============================================================

print("Congratulations! You completed the Python Week 1 basics.")