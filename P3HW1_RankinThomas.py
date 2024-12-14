# Rankin Thomas
# 12/6/24
# P3HW1 - Debugging Assignment
# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

'''
mod_1 = input('Enter grade for Module 1: ')
 mod_2 = input('Enter grade for Module 2: ')
mod_1 = input('Enter grade for Module 3: ')
mod 4 = input('Enter grade for Module 1: ')
mod_5 = input('Enter grade for Module 5: ')
 mod_6 = input('Enter grade for Module 6: ")
'''
mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))


# add grades entered to a list

# grades = [mod_1 mod2, mod_3, mod_4, Mod_5]
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6] 
# TO DO: determine lowest, highest , sum and average for grades

low = min(Grades)
high = max(grades)
total = sum(grades)
avg =sum(grades)/ len(grades)

print("\n-----------Results------------")
print(f'{"Lowest Grade:"<20}{low}')
print(f'{"Highest Grade:"<20{high}'}
print(f'{"Sum of Grades:"<20{total}'}
print(f'{"Average:"<20}{avg:.2f}'}
print("---------------------------------------")



# determine letter grade for average
if avg >= 90:
    print('Your grade is: A')   
elif avg >= 80:    
    print('Your grade is: B')
elif avg >= 70:    
    print('Your grade is: C')
elif avg >= 60:    
    print('Your grade is: D')
else:    
    print('Your grade is: F')# TO DO: finish this

'''
else:
    if avg > 80:
        print('Your grade is: B')
    else:
'''
else:
    print('Your grade is: F') 



