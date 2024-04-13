# Jeremiah Louis-Pierre
# 04/11/2024
# P5HW
# This program simulates a math quiz.
# The program displays a menu of 3 options for the user to choose from:
#   1: to add random numbers
#   2: to subtract random numbers
#   3: to exit the program

# if user enters 1, the program executes a function that 
# generates the numbers, adds them, asks user for enter an answer and displays results.

# if user enters 2, the program executes a function that 
# generates the numbers, subtracts them, asks user for enter an answer and displays results.

# if the user enters 3, the program terminates.

# if the user enters anything other than 1, 2, or 3, an error message displays letting the user know, then the menu displays again.

# when the user is in one of the functions, and they guess the right number, 
# the program congratulates them and displays the menu again to give them the option to play again

import random

def main():
    # dictionary used to assign an option to each number
    options = {1 : "Adding Random Numbers",
               2 : "Subtracting Random Numbers",
               3 : "Exit"}
    
    # initialization of answer. this is used for the loop condition.
    selection = 0
    
    print("Welcome to Math Quiz")
    print()
    
    while selection != 3:
        try:
            print()
            print("MAIN MENU")
            print('-----------------------')

            # Displays each number and option sequentially
            for num, option in options.items():
                print(f"{num}. {option}")
            
            print()
            
            # gets the user's selection
            selection = int(input("Please choose one of the menu options: ").strip())

            # loop that continues as long as the user's option is not one of the displayed options
            while selection not in options:
                print("You did not enter one of the displayed menu options")
                selection = int(input("Please choose one of the menu options again: ").strip())
        
        # used to catch if the user entered anything that's not a whole number
        except ValueError:
            print("Error occured!")
            print("Please make sure you're only entering a whole number")
            
        if selection == 1:
            adding()
        
        elif selection == 2:
            subtracting()
        
        elif selection == 3:
            print("Thank you for playing...")
            print("Bye!!")
            break


def subtracting() -> None:
    num1, num2, guesses = random.randint(1,100), random.randint(1,100), 0

    # Matches up the two numbers on display
    print(f'  {num1}')
    print(f'- {num2}')
    print()

    answer = int(input("Enter answer: ").strip())

    # tallies up first answer attempt
    guesses += 1
    
    while answer != (num1 - num2):
        if answer > (num1 - num2):
            print("Sorry, guess is too high")
            print()
            answer = int(input("Try again: ").strip())
        
        else:
            print("Sorry, guess is too low")
            print()
            answer = int(input("Try again: ").strip())
        
        # tallies up each answer attempt until the answer is correct
        guesses += 1
    
    print("Congratulations!!!! Your answer is correct.")
    print(f"Number of guesses: {guesses}")
            

def adding() -> None:
    num1, num2, guesses = random.randint(1,100), random.randint(1,100), 0

    # Matches up the two numbers on display
    print(f'  {num1}')
    print(f'+ {num2}')
    print()

    answer = int(input("Enter answer: ").strip())
    
    # tallies up each answer attempt
    guesses += 1
    
    while answer != (num1 + num2):
        if answer > (num1 + num2):
            print("Sorry, guess is too high")
            print()
            answer = int(input("Try again: ").strip())
        
        else:
            print("Sorry, guess is too low")
            print()
            answer = int(input("Try again: ").strip())
        
        # tallies up each answer attempt until the answer is correct
        guesses += 1
    
    print("Congratulations!!!! Your answer is correct.")
    print(f"Number of guesses: {guesses}")


main()

        

            





