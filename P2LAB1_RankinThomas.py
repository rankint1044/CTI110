# Thomas Rankin
# 12/6/2024
# P2Lab1_RankinThomas
# A program that calculates the diameter, circumference, and area of a circle based on user-provided radius.
 
# Import the math module for using the value of pi
import math
 
# Prompt the user to enter the radius as a float
radius = float(input("Enter the radius of the circle: "))
 
# Calculate the diameter, circumference, and area using the formulas
diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2
 
# Display the results with appropriate formatting
print(f"Diameter: {diameter:.1f}")
print(f"Circumference: {circumference:.2f}")
print(f"Area: {area:.3f}")
