# ============================================================
# PYTHON STRING MANIPULATION
# Beginner Guide
# ============================================================
#
# Strings are used to store text in Python.
#
# Example:
# name = "Geeta"
#
# IMPORTANT:
# Strings are IMMUTABLE.
# This means we cannot change the original string directly.
# String methods return a new string.
# ============================================================


# ============================================================
# 1. CHANGING LETTER CASE
# ============================================================

text = "hello python world"

# upper() converts all letters to uppercase.
print(text.upper())
# HELLO PYTHON WORLD

# lower() converts all letters to lowercase.
print(text.lower())
# hello python world

# capitalize() makes the first character uppercase.
print(text.capitalize())
# Hello python world

# title() makes the first letter of each word uppercase.
print(text.title())
# Hello Python World

# swapcase() changes uppercase to lowercase and lowercase to uppercase.
example = "Hello Python"
print(example.swapcase())
# hELLO pYTHON


# ============================================================
# 2. REMOVING SPACES
# ============================================================

name = "   Geeta   "

# strip() removes spaces from both sides.
print(name.strip())
# Geeta

# lstrip() removes spaces from the left side.
print(name.lstrip())
# Geeta   

# rstrip() removes spaces from the right side.
print(name.rstrip())
#    Geeta


# ============================================================
# 3. FINDING AND COUNTING TEXT
# ============================================================

message = "I am learning Python and I love Python."

# find() returns the index where the text first appears.
print(message.find("Python"))
# 15

# count() counts how many times text appears.
print(message.count("Python"))
# 2

# startswith() checks whether the string starts with specific text and return true or false.
print(message.startswith("I"))
# True

# endswith() checks whether the string ends with specific textand return true or false.
print(message.endswith("."))
# True


# ============================================================
# 4. REPLACING TEXT
# ============================================================

message = "I am learning Python."

# replace() replaces one piece of text with another.
new_message = message.replace("Python", "Artificial Intelligence")

print(new_message)
# I am learning Artificial Intelligence.


# IMPORTANT:
# replace() does not change the original string.
# Strings are immutable.

print(message)
# I am learning Python.


# ============================================================
# 5. SPLIT()
# ============================================================

# split() breaks a string into a LIST.

fruits_text = "apple,banana,mango,orange"

fruits = fruits_text.split(",")

print(fruits)
# ['apple', 'banana', 'mango', 'orange']

# We can also split a sentence into words.

sentence = "Python is easy to learn"

words = sentence.split()

print(words)
# ['Python', 'is', 'easy', 'to', 'learn']


# ============================================================
# 6. JOIN()
# ============================================================

# join() combines items from a list into one string.

fruits = ["apple", "banana", "mango"]

result = ", ".join(fruits)

print(result)
# apple, banana, mango

# Another example:

words = ["Python", "is", "fun"]

sentence = " ".join(words)

print(sentence)
# Python is fun


# ============================================================
# 7. CHECKING STRING CONTENT
# ============================================================

# isalpha() checks whether all characters are letters.

name = "Geeta"

print(name.isalpha())
# True

# isdigit() checks whether all characters are numbers.

age = "30"

print(age.isdigit())
# True

# isalnum() checks whether all characters are letters or numbers.

username = "Geeta123"

print(username.isalnum())
# True

# isspace() checks whether the string contains only spaces.

spaces = "   "

print(spaces.isspace())
# True

# islower() checks whether all letters are lowercase.

text = "hello"

print(text.islower())
# True

# isupper() checks whether all letters are uppercase.

text = "HELLO"

print(text.isupper())
# True

# istitle() checks whether the string is in title case such as This Is A Title Case.

text = "Hello Python"

print(text.istitle())
# True


# ============================================================
# 8. PADDING AND ALIGNMENT
# ============================================================

name = "Geeta"

# center() puts the string in the center.
print(name.center(20))

# ljust() moves the string toward the left.
print(name.ljust(20))

# rjust() moves the string toward the right.
print(name.rjust(20))

# zfill() adds zeros to the beginning.

number = "42"

print(number.zfill(5))
# 00042


# ============================================================
# 9. INDEXING AND SLICING
# ============================================================

word = "Python"

# Python starts indexing at 0.

print(word[0])
# P

print(word[1])
# y

print(word[2])
# t

# Negative indexing starts from the end.

print(word[-1])
# n

print(word[-2])
# o

# Slicing:
# [start:stop]
#
# The stop position is NOT included.

print(word[0:3])
# Pyt

print(word[2:5])
# tho

# Start from index 2 and go to the end.

print(word[2:])
# thon

# Start from the beginning and stop before index 4.

print(word[:4])
# Pyth

# Reverse the string.

print(word[::-1])
# nohtyP


# ============================================================
# 10. LEN() AND STRING LENGTH
# ============================================================

# len() is a Python built-in function.
# It tells us how many characters are in a string.

text = "Python"

print(len(text))
# 6

# Spaces are also counted.

text = "Hello World"

print(len(text))
# 11


# ============================================================
# BONUS: COMBINING STRING METHODS
# ============================================================

# In real Python programs, we often combine multiple methods.

user_input = "   geeta maharana   "

clean_name = user_input.strip().title()

print(clean_name)
# Geeta Maharana


# ============================================================
# BONUS: F-STRINGS
# ============================================================

name = "Geeta"
age = 30

message = f"My name is {name} and I am {age} years old."

print(message)
# My name is Geeta and I am 30 years old.


# ============================================================
# IMPORTANT CONCEPT: STRINGS ARE IMMUTABLE
# ============================================================

name = "geeta"

# This does NOT change the original string.
name.upper()

print(name)
# geeta

# We need to save the new string.

name = name.upper()

print(name)
# GEETA


# ============================================================
# QUICK REFERENCE
# ============================================================

# Change case:
# upper()
# lower()
# capitalize()
# title()
# swapcase()

# Remove spaces:
# strip()
# lstrip()
# rstrip()

# Find/check:
# find()
# count()
# startswith()
# endswith()

# Modify:
# replace()

# Convert between string/list:
# split()
# join()

# Check content:
# isalpha()
# isdigit()
# isalnum()
# isspace()
# islower()
# isupper()
# istitle()

# Formatting:
# center()
# ljust()
# rjust()
# zfill()

# Access text:
# indexing
# slicing

# Built-in function:
# len()


# ============================================================
# END
# ============================================================

print("\nString manipulation practice complete!")
 
