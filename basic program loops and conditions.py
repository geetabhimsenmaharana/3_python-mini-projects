"""
Python Basics: Loops, Conditions & Data Structures
---------------------------------------------------

A beginner-friendly reference demonstrating core Python concepts.

Topics:
- Variables and data types
- print() and input()
- Type conversion
- Operators
- Conditions
- Nested conditions
- for loops
- range()
- while loops
- break and continue
- Lists
- Dictionaries
- String methods
"""


# ============================================================
# 1. VARIABLES AND DATA TYPES
# ============================================================

name = input("enter your name: ").strip().lower()         # string
age = 30                # integer
price = 19.99           # float
is_student = True       # boolean

print("Name:", name)
print("Age:", age)
print("Price:", price)
print("Student:", is_student)

print("Type of name:", type(name))
print("Type of age:", type(age))


# ============================================================
# 2. USER INPUT AND TYPE CONVERSION
# ============================================================

user_name = input("Enter your name: ").strip()

user_age = int(input("Enter your age: "))

print("Hello,", user_name)
print("You are", user_age, "years old.")


# ============================================================
# 3. OPERATORS
# ============================================================

number = int(input("enter any number").strip())


print("Addition:", number + 5)
print("Subtraction:", number - 5)
print("Multiplication:", number * 5)
print("Division:", number / 5)
print("Remainder:", number % 3)

print("Is number greater than 5?", number > 5)
print("Is number equal to 10?", number == 10)
print("Is number not equal to 5?", number != 5)


# ============================================================
# 4. IF / ELIF / ELSE
# ============================================================

if user_age >= 18:
    print("You are an adult.")

elif user_age >= 13:
    print("You are a teenager.")

else:
    print("You are a child.")


# ============================================================
# 5. LOGICAL OPERATORS
# ============================================================

if user_age >= 18 and user_age <= 65:
    print("Working-age range.")

if user_age < 18 or user_age > 65:
    print("Outside the working-age range.")

if not is_student:
    print("You are not a student.")


# ============================================================
# 6. NESTED CONDITIONS
# ============================================================

print("Testcase: checking if your login passwords matches your password")
login_name = input("Enter any temp name: ")
login_password = input("Enter any  temp password: ")

if user_name.lower() == login_name.lower():

    entered_password = input("Enter password: ")

    if entered_password == login_password:
        print("Login successful.")
    else:
        print("Incorrect password.")

else:
    print("Username not found.")


# ============================================================
# 7. FOR LOOP
# ============================================================

print("\nNumbers 1 to 5:")

for i in range(1, 6):
    print(i)


# ============================================================
# 8. RANGE() WITH START, STOP, STEP
# ============================================================

print("\nEven numbers:")

for number in range(2, 11, 2):
    print(number)


print("\nCountdown:")

for number in range(5, 0, -1):
    print(number)


# ============================================================
# 9. LOOP THROUGH A STRING
# ============================================================

word = "Python is my fav language"

print("\nLetters in :",word)

for letter in word:
    print(letter)


# ============================================================
# 10. LOOP THROUGH A LIST
# ============================================================

fruits = ["apple", "banana", "orange", "mango"]

print("\nFruits:")

for fruit in fruits:
    print(fruit)


# ============================================================
# 11. CONTINUE
# ============================================================
# continue skips the current iteration.

print("\nNumbers except 5:")

for number in range(1, 11):

    if number == 5:
        continue

    print(number)


# ============================================================
# 12. BREAK
# ============================================================
# break stops the entire loop.

print("\nStop when number reaches 6:")

for number in range(1, 11):

    print(number)

    if number == 6:
        break


# ============================================================
# 13. CONTINUE + BREAK TOGETHER
# ============================================================

print("\nSkip 5 and stop at 8:")

for number in range(1, 11):

    if number == 5:
        continue

    print(number)

    if number == 8:
        break


# ============================================================
# 14. WHILE LOOP
# ============================================================

print("\nWhile loop:")

counter = 1

while counter <= 5:
    print(counter)
    counter = counter + 1


# ============================================================
# 15. WHILE TRUE + BREAK
# ============================================================
# while True creates a loop that continues until break.

print("\nWaiting for number 10:")

while True:

    number = int(input("Enter a number: "))

    if number < 0:
        print("Negative number skipped.")
        continue

    if number == 10:
        print("Found 10!")
        break

    print("Number entered:", number)


# ============================================================
# 16. LIST BASICS
# ============================================================

colors = ["red", "blue", "green"]

print("\nFirst color:", colors[0])

colors.append("yellow")

print("Updated list:", colors)

print("Number of colors:", len(colors))


# ============================================================
# 17. LIST SLICING
# ============================================================

numbers = [10, 20, 30, 40, 50]

print("\nFirst three numbers:", numbers[0:3])
print("Last two numbers:", numbers[-2:])


# ============================================================
# 18. DICTIONARY
# ============================================================

person = {
    "name": "Geeta",
    "age": 30,
    "city": "Boston"
}

print("\nPerson name:", person["name"])
print("Person city:", person["city"])

person["job"] = "Engineer"

print("Updated person:", person)


# ============================================================
# 19. LOOP THROUGH A DICTIONARY
# ============================================================

print("\nPerson information:")

for key, value in person.items():
    print(key, ":", value)


# ============================================================
# 20. STRING METHODS
# ============================================================

text = "  Python is Fun  "

print("\nOriginal:", text)
print("Lower:", text.lower())
print("Upper:", text.upper())
print("Stripped:", text.strip())
print("Title:", text.title())

clean_text = text.strip()

if "Python" in clean_text:
    print("Python was found in the text.")


# ============================================================
# 21. PRACTICAL MINI EXAMPLE
# ============================================================

print("\n--- Number Checker ---")

for i in range(5):

    number = int(input("Enter a number: "))

    if number < 0:
        print("Negative number skipped.")
        continue

    if number == 0:
        print("Zero entered.")
        continue

    if number % 2 == 0:
        print("Positive even number:", number)
    else:
        print("Positive odd number:", number)


# ============================================================
# END
# ============================================================

print("\nPython basics practice completed!")

