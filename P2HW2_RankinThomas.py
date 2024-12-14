# Rankin Thomas
# 12/6/24
# P2HW2 - List Operations
# This program collects grades for six modules, stores them in a list, and calculates the lowest, highest, sum, and average of the grades.

# 1. Prompt the user to input grades for Module 1 through Module 6.
# 2. Store each grade in a list named `grades`.
# 3. Calculate the following:
# Request grades for six modules and store them in a list
grades = []
grades.append(float(input("Enter grade for Module 1: ")))
grades.append(float(input("Enter grade for Module 2: ")))
grades.append(float(input("Enter grade for Module 3: ")))
grades.append(float(input("Enter grade for Module 4: ")))
grades.append(float(input("Enter grade for Module 5: ")))
grades.append(float(input("Enter grade for Module 6: ")))
 
# Calculate required values
lowest_grade = min(grades)
highest_grade = max(grades)
sum_of_grades = sum(grades)
average_grade = sum_of_grades / len(grades)
 
# Display the results
print("\n------------Results------------")
print(f"Lowest Grade:      {lowest_grade}")
print(f"Highest Grade:     {highest_grade}")
print(f"Sum of Grades:     {sum_of_grades}")
print(f"Average:           {average_grade:.2f}")
print("--------------------------------")
