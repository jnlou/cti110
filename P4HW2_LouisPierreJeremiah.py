# Jeremiah Louis-Pierre
# 03/29/2024
# P4HW2
# This program calculates gross pay for multiple employees, determined by user, 
# and also calculates total amount paid for overtime, total amount paid for regular pay and total amount paid for all employees.
# This is done by repeatedly asking for the employee's name or the word "Done", 
# if the user does not enter the word "Done", then the program asks for the number of hours the employee worked, and their pay rate.
# If the hours they entered is more than 40, then they will receive overtime pay for their overtime hours.
# Then, The program will display the following for the current employee:
#   1. Employee name
#   2. pay rate
#   3. number of hours worked
#   4. overtime hours
#   5. overtime pay
#   6. pay for regular hours 
#   7. gross pay
# Once that is done, it will once again ask for the employee's name or the word "Done".
# If the user enters the word "Done", the program will display the following:
#   1. The total number of employees entered
#   2. The total amount paid for overtime
#   3. The total amount paid for regular hours
#   4. The total amount paid in gross

# Design of program/pseudocode:
# Declare String name, names[]
# Declare Real hours, pay_rate, overtime_hours, reg_pay, overtime_pay, overtime_pay_total = 0, reg_pay_total = 0, gross_pay_total = 0
# Declare Integer counter = 0

# Display "Enter employee's name or "Done" to terminate: "
# Input name

# While name != "Done"
#   Set names[counter] = name
#   Set counter = counter + 1

#   Display "Enter number of hours worked: "
#   Input hours
    
#   Display "Enter employee's pay rate: "
#   Input pay_rate
    
#   If hours > 40 Then
#     Set overtime_hours = hours - 40
#   Else
#     Set overtime_hours = 0
#   End If
    
#   Set reg_pay = pay_rate * (hours - overtime_hours)
#   Set reg_pay_total = reg_pay_total + reg_pay
    
#   Set overtime_pay = (pay_rate * 1.5) * overtime_hours
#   Set overtime_pay_total = overtime_pay_total + overtime_pay
    
#   Set gross_pay_total = gross_pay_total + (reg_pay + overtime_pay)
    
#   Display "Employee name: ", name
#   Display "Hours Worked    Pay Rate    Overtime    Overtime Pay    RegHour Pay    Gross Pay"
#   Display hours, pay_rate, overtime_hours, overtime_pay, reg_pay, reg_pay + overtime_pay

#   Display "Enter employee's name or "Done" to terminate: "
#   Input name
# End While

# Display "Total number of employees entered: ", length(names)
# Display "Total amount paid for overtime: $", overtime_pay_total
# Display "Total amount paid for regular hours: $", reg_pay_total
# Display "Total amount paid in gross: $", gross_pay_total

names, overtime_pay_total, reg_pay_total, gross_pay_total = [], 0, 0, 0
name = input(f"Enter employee's name or 'Done' to terminate: ").strip().title()
while name != "Done":
    names.append(name)
    hours = float(input("Enter number of hours worked: ").strip())
    pay_rate = float(input("Enter employee's pay rate: ").strip())

    # this calculation returns a remainder of potential extra hours that may be on top of the regular 40
    # For example: if hours = 43, overtime_hours would be 43 - 40 which equals 3. This means there were 3 additional hours.
    overtime_hours = hours - 40 if hours > 40 else 0

    # this means whether if the hours is greater than 40 or not, it'll always be multiplying correctly by however many extra hours the person may have worked
    # For example: if the pay rate is 9 and "hours" is 41, then "reg_pay" would be: 9 * (41 - 1) which would be 9 * 40 which equals 360 
    reg_pay = pay_rate * (hours - overtime_hours)
    reg_pay_total += reg_pay

    # This calculation creates a new pay rate then multiplies by however many extra hours the person worked
    overtime_pay = (pay_rate * 1.5) * overtime_hours
    overtime_pay_total += overtime_pay

    gross_pay_total += reg_pay + overtime_pay

    print(f"Employee name:      {name}")
    print(f"Hours Worked    Pay Rate    Overtime    Overtime Pay    RegHour Pay    Gross Pay")
    print(f"----------------------------------------------------------------------------------------")
    print(f"{hours:<15.1f} ${pay_rate:<11,.2f} {overtime_hours:<11.1f} ${overtime_pay:<15,.2f} ${reg_pay:<14,.2f} ${reg_pay + overtime_pay:,.2f}")
    print()
    name = input(f"Enter employee's name or 'Done' to terminate: ").strip().title()

print(f'Total number of employees entered: {len(names)}')
print(f'Total amount paid for overtime: ${overtime_pay_total}')
print(f'Total amount paid for regular hours: ${reg_pay_total}')
print(f'Total amount paid in gross: ${gross_pay_total}')


