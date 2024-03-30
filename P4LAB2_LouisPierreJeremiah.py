# Jeremiah Louis-Pierre
# 03/27/2024
# P4LAB2
# This program takes two integers. If the second integer is smaller than the first integer,
# the program stops and tells the user that the second integer can't be less than the first.
# Else, the first integer is displayed and increments by 5 as long as it's less than or equal to the second integer.
num1 = int(input("Enter the first integer: ").strip())
num2 = int(input("Enter the second integer: ").strip())
if num2 < num1:
    print("Second integer can't be less than the first.")

else:

    while num1 <= num2:
        print(num1, end = ' ')

        if num1 + 5 > num2:
            print("\n", end = '')
            break
        
        else:
            num1 += 5