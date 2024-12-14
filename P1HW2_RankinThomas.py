# Thomas Rankin
# 12/4/2024
# P1HW2 - Travel Budget Calculator
# This program calculates the total expenses for a trip and determines the remaining budget.
 
# Step 1: Ask for user inputs
budget = float(input("Enter your budget: "))  # User's budget
destination = input("Enter your travel destination: ")  # Travel destination
gas = float(input("Enter the amount you will spend on gas: "))  # Gas expenses
accommodation = float(input("Enter the amount you will spend on accommodation: "))  # Accommodation expenses
food = float(input("Enter the amount you will spend on food: "))  # Food expenses
 
# Step 2: Calculate total expenses and remaining budget
total_expenses = gas + accommodation + food  # Add all expenses
remaining_budget = budget - total_expenses  # Subtract expenses from budget
 
# Step 3: Display the results
print("\n------------Travel Expenses------------")
print(f"Location: {destination}")
print(f"Initial Budget: ${budget:.2f}")
print(f"Fuel: ${gas:.2f}")
print(f"Accommodation: ${accommodation:.2f}")
print(f"Food: ${food:.2f}")
print("----------------------------------------")
print(f"Remaining Budget: ${remaining_budget:.2f}")
