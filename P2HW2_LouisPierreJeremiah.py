# Jeremiah Louis-Pierre
# 2/21/2024
# P2HW2
# This program takes a user's grade from each test, then displays the following:
# 1. The lowest grade
# 2. The highest grade
# 3. The sum of all grades
# 4. The grades' average

# Layout of this code (aka the pseudocode/design)
#(Note: I will be using the min(), max() and sum() functions,
# but, I feel that just writing them as is wouldn't be considered pseudocode.
# so, i'll write them in a way that will fit as pseudocode)

# Declare Real grades[6]
# Declare Real lowest = grades[0], highest = grades[0], total = 0, average
# For i = 1 to 7
    # Display "Enter your grade for module", i
    # Input grades[i]
# For index = 0 to 5
    # If grades[index] < lowest Then
        # Set lowest = grades[index]
    # If grades[index] > highest Then
        # Set highest = grades[index]
    # Set total = total + grades[index]
# Set average = total / 5

# Display "Lowest grade: ", lowest
# Display "Highest grade: ", highest
# Display "Sum of all grades: ", total
# Display "Average of all grades: ", average
    

grades = []
for i in range(1,7):
    grade = float(input(f"Enter your grade for module {i}: ").strip())
    grades.append(grade)
print("------------Results------------")
print(f"{'Lowest grade:':<15}{min(grades):>14,.2f}")
print(f"{'Highest grade:':<15}{max(grades):>14,.2f}")
print(f"{'Sum of all grades:':<15}{sum(grades):>12,.2f}")
print(f"{'Average of all grades:':<15}{sum(grades) / len(grades):>7.2f}")
print("----------------------------------------")
