# Thomas Rankin
# 12/4/2024
# P1HW1
# This program performs two mathematical operations:
#It calculates the result of raising a base number to an exponent.
# It adds two integers and subtracts a third from their sum.
 
# Step 1: Calculate the base raised to the power of an exponent
base = int(input("Enter an integer for the base value: "))
exponent = int(input("Enter an integer for the exponent value: "))
result = base ** exponent
print(f"{base} raised to the power of {exponent} is {result}!")
 
# Step 2: Add two integers and subtract a third
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))
calculation = (num1 + num2) - num3
print(f"The result of adding {num1} and {num2}, then subtracting {num3}, is {calculation}!")
