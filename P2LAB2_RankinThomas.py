# Thomas Rankin
# 12/6/2024
# P2LAB2
# A program that uses a dictionary to store automobile MPG data and calculates gas usage based on user input.
 
# Create a dictionary with automobiles and their MPG values
car_mpg = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
     "Silverado": 26 }
 
# Create a variable holding all keys in the dictionary
keys = car_mpg.keys()
 
# Print the variable holding the keys
print("Available vehicles:", keys)
 
# Prompt the user to enter one of the vehicles from the dictionary
vehicle = input("Enter a vehicle from the list above: ")
 
# Check if the entered vehicle exists in the dictionary
if vehicle in car_mpg:
     mpg = car_mpg[vehicle]
     print(f"The MPG for the {vehicle} is {mpg}.")
     
     # Prompt the user to enter the number of miles they plan to drive
     miles = float(input(f"How many miles will you drive the {vehicle}? "))
     
     # Calculate the gallons of gas needed
     gallons_needed = miles / mpg
     
     # Display the gallons of gas needed, rounded to two decimal places
     print(f"To drive {miles} miles in the {vehicle}, you will need {gallons_needed:.2f} gallons of gas.")
else:
    print("Error: The entered vehicle is not in the list.")
