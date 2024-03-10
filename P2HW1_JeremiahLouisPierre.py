# Jeremiah Louis-Pierre
# 2/21/2024
# P2HW1
# This project calculates and displays travel expenses


budget = float(input("Enter Budget: "))
destination = input("Enter your travel destination: ").title()
gas = float(input("How much do you think you will spend on gas?: "))
accommodation = float(input("Approximately, how much will you need for accomodation/hotel?: "))
food = float(input("Last, how much do you need for food?: "))

# Each format has a comma specifier even if they don't need one, this is for use cases when the user does plan to spend a hefty amount
print("------------Travel Expenses------------")
print(f"{'Location:':<12}{destination:>10}")
print(f"{'Initial budget:':<12} {'$':>5}{budget:<12,.2f}")
print(f"{'Fuel:':<12} {'$':>8}{gas:<11,.2f}")
print(f"{'Accommodation:':<12} {'$':>6}{accommodation:<13,.2f}")
print(f"{'Food:':<12}  {'$':>7}{food:<14,.2f}")
print("---------------------------------------")
print(f"{'Remaining balance:':<12} {'$':>2}{budget - sum([gas, accommodation, food]):<12,.2f}")

