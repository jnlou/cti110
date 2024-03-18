# Jeremiah Louis-Pierre
# 3/1/2024
# P3LAB
# This program determines if a year is a leap year.
# This is determined based on two conditions:
#   1) The year must be divisible by 4.
#   2) If the year is a century year, the year must be evenly divisible by 400.

input_year = int(input("Enter a year: ").strip())
# turned the number input into a string for the purpose of referring to the index of its ending numbers
# This means if the year given is a century year, then see if it's divisible by 400
if str(input_year)[-2:] == '00':
    if input_year % 400 != 0:
        print(f"{input_year} - not a leap year")
    else:
        print(f"{input_year} - leap year")
else:
    if input_year % 4 != 0:
        print(f"{input_year} - not a leap year")
    else:
        print(f"{input_year} - leap year")
