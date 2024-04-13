# Jeremiah Louis-Pierre
# 04/11/2024
# P5LAB
# I decided to start using type annotations in function headers, 
# and since it looks a bit different than what i usually write, i'll break down each header and explain what it means
# This program simulates grocery shopping.
#    Firstly, the program displays all available items to be purchase, along with their prices.
#    Then the program repeatedly prompts the user to enter an item from the displayed items or enter the word "end" to stop
#    Secondly, the program displays every item in the user's cart, along with the quantity of each item

#    Thirdly, the program display a receipt for the user. Which showcases every item in the user's cart, 
#    along with the quantity of each item, as well as the combined price of each item. 
#    On the same display, the program shows the subtotal, the tax of the subtotal, then a complete total of every item in the user's cart.

#    Fourthly, the program repeatedly displays the complete total and tells the user that it's what they owe to complete the purchase.
#    Along with that, the program also repeatedly prompts the user to enter cash into the self-checkout machine, to pay for the total.
#    After the total is successfully paid for, the program displays how much change is leftover to be dispensed to the user, if there is any.

#   Lastly, if there's change leftover that's owed to the user, the program calculates how many dollars, quarters, dimes, nickels, and pennies
#   that's to be dispensed to the user. Which the program then displays and provides to the user.
#   Or, if there weren't any change leftover, meaning if the user paid the exact amount of the total, the progra displays that there aren't any change to be owed to them.


def main():
    groceries = {"apples": 3.69,
                 "berries" : 4.00,
                 "chocolate" : 2.89,
                 "turkey" : 6.99,
                 "cheese" : 4.00,
                 "pepsi" : 7.89,
                 "eggs" : 3.50,
                 "bread" : 3.00 
                }
    
    show_avail_items(groceries)
    print()

    cart = grocery_checkout(groceries)
    print()
    
    revised_cart = show_cart(cart)
    print()
    
    total = calc_total(revised_cart, groceries)
    print()
    
    change = self_checkout(total)
    print()
    
    # if "change" has value (meaning if it's larger than 0), this means there's change owed to the user.
    if change:
        print('Dispensing...')
        print()
        
        # transferred the exact code from "P5LAB_ALL.py"
        # since the functionality in that module requires an integer, 
        # the decimal from the floating-point number "change" must get moved two places to the right as "disperse_change()" gets called
        # and since formatting such as ".2f" rounds to the nearest place specified by the decimal point and the number next to the f (in this case 2),
        # "change" may or may not be rounded properly when getting returned from "self_checkout()".
        # so to ensure the number is properly rounded, "round(change * 100)" first moves the decimal place 2 places to the right,
        # then rounds the number as an integer. this way it'll always receive the correct number to lend change to
        disperse_change(round(change * 100))
    
    else:
        print("You have no change to be owed to you")
    print()
    print("Thanks for shopping!")

    

# definition; 
# parameters: "groceries" is a dictionary that contains string as a key, and floating-point number(s) as a value
# return value: None, otherwise known as a void function
def show_avail_items(groceries: dict[str: float]) -> None:
    print(f"{'Grocery Item':<25}{'Price'}")
    print('------------------------------')
    
    for item, price in groceries.items():
        print(f"{item:<24} ${price:,.2f}")
    print('------------------------------')

# definition;
# parameters: "groceries" is a dictionary that contains string as a key, and floating-point number(s) as a value
# return value: a list of strings
def grocery_checkout(groceries: dict[str: float]) -> list[str]:
    cart, item = [], ''

    print("*Welcome to the Grocery Checkout*")
    print()
    
    # prompts the user to enter an item
    item = input('Enter an item to add to the cart or type "end" to stop adding items: ').lower().strip()
    
    while item != 'end':
        try:
            # This statement iterates through "item" to see if any element is not an alphabetical letter
            # if it is, then a ValueError exception gets raised
            if any(not i.isalpha() for i in item):
                raise ValueError
            
            # else if "item" is not in "groceries", a message displays that it is not in stock.
            elif item not in groceries:
                print("That item is not in stock")
                print()

            # if both conditions are not met, than the item gets added to the user's cart, with a message confirming that. 
            else:
                cart.append(item)
                print(f"{item} was added to your cart.")
            
        except ValueError:
            print("Error occured!")
            print("Please make sure you're only entering letters")
            print()
        
        # this is to ensure that no matter if an error happens or not, the program repeatedly prompts the user to enter an item.
        # this is used to continue the loop for as long as "item" doesn't equal "end".
        finally:
            item = input('Enter an item to add to the cart or type "end" to stop adding items: ').lower().strip()
    
    # returns the cart
    return cart

# definition;
# parameters: "cart" is a list of strings
# return value: a dictionary that contains string as a key, and integer(s) as a value
def show_cart(cart: list[str]) -> dict[str: int]:

    # dictionary comprehension that contains the item, and the count of every occurence of the item inside of the user's cart
    # this works out because in dictionaries, there can only be one of the same name as a key. 
    # so for example, you can't have two "bread"'s as a key in the dictionary, all that happens is it'll update the value for the "bread" key.
    user_cart = {i : cart.count(i) for i in cart}
    
    # if the dictonary is empty, then the program displays that the user's cart is empty
    if not user_cart:
        print("Your cart is empty")

    else:
        print("The items currently in your cart are:")
        
        # Displays the item, as well as the quantity of the item, in the user's cart
        for item, quantity in user_cart.items():
            print(f"{item:<8} x{quantity}")

    # returns the dictionary of items the user added to their shopping cart and each item's quantity, 
    # but in a way where there aren't any repeating words
    return user_cart


# definition;
# parameters: "cart" is a dictionary that contains string as a key, and integer(s) as a value, 
#             "groceries" is a dictionary that contains string as a key, and floating-point number(s) as a value
# return value: a floating-point number
def calc_total(cart: dict[str: int], groceries: dict[str: float]) -> float:
    subtotal, food_tax = 0, .02
    print("Grocery Checkout Receipt")
    print("-------------------------------")

    # displays the item, it's quanity and its price.
    # using the key represented by "item", "groceries[item]" grabs the price of the item from the adjacent key.
    # considering that the multiple of the same item would of course, change the price because of it being multiple of the same item,
    # "groceries[item] * quantity" multiplies the price of the item times however many of that item the user added, displaying a full total for that specific item
    for item, quantity in cart.items():
        print(f"{item} x{quantity:<14} ${groceries[item] * quantity:,.2f}")

        # since the user may add more than one of the same item, this adds the full total for that specific item
        subtotal += (groceries[item] * quantity)

    print(f"{'SUBTOTAL:':<15} ${subtotal:,.2f}")
    print()

    tax = subtotal * food_tax

    print(f"{'TAX:':<15} ${tax:,.2f}")
    print(f"{'TOTAL:':<15} ${subtotal + tax:,.2f}")

    return subtotal + tax

    
        
                 

# definition;
# parameters: "total" is a floating-point number
# return value: a floating-point number
def self_checkout(total: float) -> float:
     
    # while the total has value (meaning while "total" is > 0),
    # this loop will repeatedly prompt the user to put cash into the self-checkout machine
    while total:
        try:
            print()
            print(f"You owe ${total:,.2f} for the groceries")
            print()
            cash = float(input("How much cash will you put in the self-checkout machine?: $").strip())
            
            # well you obviously can't pay with a negative amount of money
            if cash < 0:
                print("Error occured!")
                print("Please make sure you're only entering non-negative numbers")
            
            else:
                print(f"${cash:,.2f} was entered into the self-checkout machine. ")
                if cash > total:
                   print()
                   print(f"The change owed to you is ${(cash - total):,.2f}")

                   # returns the change here since the cash outweighs the total, meaning there's guarenteed change to be owed to the user
                   return cash - total

                else:
                    # decrements the total by however much cash the user adds to the self-checkout machine
                    total -= cash
        
        except ValueError:
            print("Error occured!")
            print("Please make sure you're only entering numbers.")
    
    # if the entire loop finishes, then it means there was never an event where the cash the user inserted was larger than however much was owed.
    # in other words, it means the user must have paid the exact amount. so this returns 0, indicating there's no change owed to the user.
    return 0


# definition;
# parameters: "change" is an integer
# return value: None, otherwise known as a void function
def disperse_change(change: int) -> None:
#Calculate the amount of each coin needed
#integer division - //
    num_dollars = change // 100
    change = change - (num_dollars * 100)

    num_quarters = change // 25
    change = change - (num_quarters * 25)

    num_dimes = change // 10
    change = change - (num_dimes * 10)

    num_nickles = change // 5
    change = change - (num_nickles *5)

    num_pennies = change // 1

    #Display coins owed

    if num_dollars > 0:
            print(num_dollars,  end=" ")
            if num_dollars == 1:
                print("Dollar")
            else:
                print("Dollars")

    if num_quarters > 0:
            print(num_quarters,  end=" ")
            if num_quarters == 1:
                print("Quarter")
            else:
                print("Quarters")

    if num_dimes > 0:
            print(num_dimes,  end=" ")
            if num_dimes == 1:
                print("Dime")
            else:
                print("Dimes")

    if num_nickles > 0:
            print(num_nickles,  end=" ")
            if num_nickles == 1:
                print("Nickle")
            else:
                print("Nickles")

    if num_pennies > 0:
            print(num_pennies,  end=" ")
            if num_pennies == 1:
                print("Penny")
            else:
                print("Pennies")
    

main()