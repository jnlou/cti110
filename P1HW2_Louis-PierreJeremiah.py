# Jeremiah Louis-Pierre
# 2/12/2024
# P1HW2
# This project calculates and displays travel expenses


budget = float(input("Enter Budget: "))
destination = input("Enter your travel destination: ").title()
gas = float(input("How much do you think you will spend on gas?: "))
accommodation = float(input("Approximately, how much will you need for accomodation/hotel?: "))
food = float(input("Last, how much do you need for food?: "))

print("------------Travel Expenses------------")
print(f"Location: {destination}")
print(f'Initial budget: ${budget}')
print()
print(f'Fuel: ${gas}')
print(f"Accommodation: ${accommodation}")
print(f"Food: ${food}")
print()
print(f"Remaining balance: ${budget - sum([gas, accommodation, food])}")

