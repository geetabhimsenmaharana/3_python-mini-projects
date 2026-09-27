

# ============================================================
# 15. MINI CALCULATOR
# ============================================================

# Ask the user to select an operator.

operator = input("Choose an operator (+, -, *, /): ")

# Ask the user for two numbers.

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform the correct calculation.

if operator == "+":
    result = num1 + num2

elif operator == "-":
    result = num1 - num2

elif operator == "*":
    result = num1 * num2

elif operator == "/":

    # Check that the user isn't trying to divide by zero.

    if num2 != 0:
        result = num1 / num2
    else:
        result = "Cannot divide by zero."

else:
    result = "Invalid operator."

print(f"Result: {result}")
