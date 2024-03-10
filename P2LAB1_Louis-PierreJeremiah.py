# Jeremiah Louis-Pierre
# 02/21/2025
# P2LAB1
# This program takes a user's gas mileage and cost of gas, 
# and outputs the gas cost for 20 miles, 75 miles, and 500 miles


mileage = float(input("Enter the car's gas mileage: ").strip())
gas_cost = float(input("Enter the price of gas: ").strip())
print(f"Mileage: {mileage:.2f}")
print(f"Gas cost: ${gas_cost:.2f}")
print(f"Gas cost for 20 miles: ${(20 / mileage) * gas_cost:.2f}")
print(f"Gas cost for 75 miles: ${(75 / mileage) * gas_cost:.2f}")
print(f"Gas cost for 500 miles: ${(500 / mileage) * gas_cost:.2f}")

