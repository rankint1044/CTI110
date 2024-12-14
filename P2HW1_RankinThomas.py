# Thomas Rankin
# 12/6/2024
# P2HW1
# A program to calculate and display travel costs, formatted with proper alignment and monetary formatting.
 
# Prompt the user to enter the destination
destination = input("Enter your travel destination: ")
 
# Prompt the user to enter the budget as a float
budget = float(input("Enter your travel budget: "))
 
# Prompt the user to enter the travel costs and accommodation costs as floats
gas_cost = float(input("Enter the estimated cost for gas: "))
accommodation_cost = float(input("Enter the estimated cost for accommodation: "))
food_cost = float(input("Enter the estimated cost for food: "))

# Calculate the remaining budget
remaining_budget = budget - (gas_cost + accommodation_cost + food_cost)
 
# Display the results in a nicely formatted way
print("\n------------Travel Expenses------------")
print(f"{'Destination:':<20}{destination}")
print(f"{'Initial Budget:':<20}${budget:,.2f}")
print(f"{'Gas:':<20}${gas_cost:,.2f}")
print(f"{'Accommodation:':<20}${accommodation_cost:,.2f}")
print(f"{'Food:':<20}${food_cost:,.2f}")
