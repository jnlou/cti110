# Jeremiah Louis-Pierre
# 03/27/2024
# P4HW1
# This program takes a number of scores, then determines the average and displays the letter grade that represents the average.
# This time, the determination of the letter grade for the average is done through an iteration of a list of a range of numbers and the corresponding letter that represents that list

# Design of program/pseudocode:
# Declare Dictionary(String letter, Integer numbers[10]) letter_and_grade
# Declare Integer i, counter = 1, scores_num, digits[10]
# Declare Real score, average, sum = 0
# Declare String grade = "", current_letter

# While counter <= 10
#   For i = 90 To 100 
#     Set letter_and_grade["A"]numbers[counter] = i
#     Set counter = counter + 1
#   End For
# End While

# Set counter = 1
# While counter <= 10
#   For i = 80 To 90 
#     Set letter_and_grade["B"]numbers[counter] = i
#     Set counter = counter + 1
#   End For
# End While

# Set counter = 1
# While counter <= 10
#   For i = 70 To 80 
#     Set letter_and_grade["C"]numbers[counter] = i
#     Set counter = counter + 1
#   End For
# End While 

# Set counter = 1
# While counter <= 10
#   For i = 60 To 70 
#     Set letter_and_grade["D"]numbers[counter] = i
#     Set counter = counter + 1
#   End For
# End While

# While True
#   Try
#       Display "Enter the number of scores you would like to enter: "
#       Input scores_num

#       While scores_num < 2
#           Display "Entered number must be at least 2."
#           Input scores_num
#       End While
#       Break
#   Catch exception ValueError
#       Display "Input must be an integer, try again"
#   End Try
# End While

# Declare Real scores[scores_num]

# For i = 0 To scores_num
#   Try
#       Display "Enter score #", i + 1, ": "
#       Input score

#       While score < 0 OR score > 100
#           Display "INVALID Score entered!!!!"
#           Display "Score should be between 0 and 100."
#           Display "Enter score #", i + 1, "again: "
#           Input score
#       End While

#   Catch exception ValueError
#       While True
#           Try
#               Display "INVALID Score entered!!!!"
#               Display "Input must be a number"

#               Display "Enter score #", i + 1, "again: "
#               Input score
#               Break
#           Catch exception ValueError
#               Display "Input still is not a number, try again"
#           End Try

#       End While
#   End Try

#   Set scores[i] = score
# End For

# Declare lowest = scores[0]
# For i = 0 To length(scores)
#   If scores[i] < lowest Then
#       Set lowest = scores[i]
#   End If
# End For

# delete(scores, lowest)

# For i = 0 To length(scores)
#   Set sum = sum + scores[i]
# End For
# Set average = sum / (scores_num - 1)

# For Each current_letter = letter, digits[10] = numbers[10] In letter_and_grade
#   If average In digits Then
#       Set grade = current_letter
#       Break
#   End If
# End For
# If length(grade) < 1 Then
#   Set grade = "F"
# End If

# Display "------------Results------------"
# Display "Lowest Score :", lowest
# Display "Modified List :", scores
# Display "Scores Average :", average
# Display "Grade :", grade
# Display "----------------------------------------"





# a dictionary where each key-value pair contains a letter grade, and a list of numbers that matches the criteria for the letter grade
letter_and_grade = {'A' : [i for i in range(90,101)],
                    'B' : [i for i in range(80,90)],
                    'C' : [i for i in range(70,80)],
                    'D' : [i for i in range(60,70)],
                    }

# A continuous loop that repeats indefinitely for the purpose of always catching a ValueError
# This means if the user enters either a floating-point or a non-digit value, it will always catch this error,
# and repeatedly prompt the user to re-enter a number until the value entered is an integer.
while True:
    try:
        scores_num = int(input("Enter the number of scores you would like to enter: ").strip())
        
        # When the lowest element of the 'scores' gets removed later, there has to be another number in the list or it'll raise an exception,
        # meaning there has to be at least 2 elements in the 'scores' list, so this loop continues as long as the user enters a number that's less than 2.
        while scores_num < 2:
            print("Entered number must be at least 2.")
            scores_num = int(input("Enter the number of scores you would like to enter again: ").strip())
        
        # breaks out of infinite loop if it meets the condition of the value being at least 2
        break
    
    except ValueError:
        print("Input must be an integer, try again")

# initialization of a list containing score numbers
scores = []  

# a loop that continues "scores_num" times
for i in range(scores_num):
        # used to catch a ValueError exception that would be caused by the user not entering a digit
        try:
            score = float(input(f"Enter score #{i + 1}: ").strip())
            # the score must be in the range of 0-100,
            # so this loop will continue as long as the user doesn't enter a number in that range
            while score < 0 or score > 100:
                # Empty space used to separate from recent output
                print()

                print("INVALID Score entered!!!!")
                print("Score should be between 0 and 100.")
                
                # prompts the user to enter the current number's score again
                score = float(input(f"Enter score #{i + 1} again: ").strip())
        
        except ValueError:
            # used to separate the original prompt, and the repetition of a another prompt
            print()

            # this would-be infinite loop and try-except block was honestly used so that a new prompt could include the word "again",
            # since a new prompt from the problem of the user entering an invalid score has the word "again" in it.

            # But, this loop runs indefinitely until the "break" statement is reached. In order for that to happen,
            # a ValueError exception can't get raised from the user's entered value
            while True:
                try:
                    # Displays what the problem is and what is to be expected from the input from the user
                    print("INVALID Score entered!!!!")
                    print("Input must be a number")

                    # prompts the user to enter the current number's score again
                    score = float(input(f'Enter score #{i + 1} again: ').strip())

                    while score < 0 or score > 100:
                        # Empty space used to separate from recent output
                        print()

                        print("INVALID Score entered!!!!")
                        print("Score should be between 0 and 100.")

                        # prompts the user to enter the current number's score again
                        score = float(input(f"Enter score #{i + 1} again: ").strip())
                    
                    # breaks out of the infinite loop if the while loop condition isn't met
                    break
                
                # Since this handler is inside a would-be infinite loop,
                # it'll just return back to the lines that display what the issue is.
                # So it's purpose is to separate its recent prompt to a another prompt.
                except ValueError:
                    print()

        # after the correct value type is entered, it appends it to the 'scores' list
        scores.append(score)


# retrieves the minimum value in the 'scores' list
lowest = min(scores)

# removes the minimum value in the 'scores' list
scores.remove(lowest)

# initalizes an empty string that will get filled later
grade, average = '', sum(scores) / len(scores)

# this loop iterates through the 'letter_and_grade' dictionary using two variables,
# 'letter' to represent the letter grade key, and 'nums' to represent the list of numbers to the corresponding key
for letter, nums in letter_and_grade.items():
    
    # if the integer value of the average is in a list of numbers, then its corresponding letter is assigned to the 'grade' variable
    # For example: if the average is 78.67, the integer value of this is just 78. So what's being tested in each iteration,
    # is the number 78.
    if int(average) in nums:
        grade = letter

        # since a letter has been assigned, break out of the loop
        break

# if the entire loop through the dictionary is complete, this means the average was not found in any list,
# and since the keys contain letters A-D, the only letter left out is F.
# So the grade letter is assigned to this left out letter, F.
if not grade:
    grade = 'F'
    

print("------------Results------------")
print(f"{'Lowest Score  :':<15}{lowest:>7.1f}")
print(f"{'Modified List :':<15} {scores}")
print(f"{'Scores Average:':<15}{average:>7.2f}")
print(f"{'Grade         :':<15}{grade:>3}")
print("----------------------------------------")
