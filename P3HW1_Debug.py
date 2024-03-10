# Jeremiah Louis-Pierre
# 03/14/24
# P3HW1
# This program takes a number of grades, then determines the average and displays the letter grade that represents the average.


# Enter grades for six modules, and add them to a list 

grades = []
for i in range(1,7):
    module = float(input(f'Enter grade for Module {i}: ').strip())
    grades.append(module)

# TO DO: determine lowest, highest , sum and average for grades
    
# only set the average to a variable to prepare for the number of if-statements later,
# would rather only type the variable name than to constantly type the operation
avg = sum(grades) / len(grades)
print('------------Results------------')
print(f'Lowest Grade:       {min(grades):.1f}')
print(f'Highest Grade:      {max(grades):.1f}')
print(f'Sum of Grades:      {sum(grades):.1f}')
print(f'Average:            {sum(grades) / len(grades):.2f}')
print('-------------------------------------------')

# determine letter grade for average
if avg >= 90:
    print('Your grade is: A')
elif avg > 79 and avg <= 89:
    print('Your grade is: B')
elif avg > 69 and avg <= 79:
    print('Your grade is: C')
elif avg > 59 and avg <= 69:
    print('Your grade is: D')
else:
    print('Your grade is: F')
