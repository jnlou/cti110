# Jeremiah Louis-Pierre
# 02/21/2024
# P2LAB2
# This program takes 4 floating-point numbers,
# then displays their product, their rounded average as integers, 
# then their averages as floating-point numbers

nums = []
total = 1

for i in range(1,5):
    number = float(input(f"Enter number #{i}: ").strip())
    nums.append(number)
    total *= number

print(f"Their product as an integer: {round(total)}; Their average as an integer: {round(sum(nums) // len(nums))}")
print(f"Their product as a floating-point number : {total:.3f}; Their average as a floating-point number: {sum(nums) / len(nums):.3f}")
