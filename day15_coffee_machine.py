## Coffee Machine

import menu

supplies = menu.resources   # store supply dictionary from menu.py
menu_items = menu.MENU      # store menu dictionary from menu.py
is_on = True                # sets machine state to on
profit = 0                  # initial profit is $0

# function to get the users menu choice
def selection(menu_items):
    print(f"Menu:\nEspresso ${menu_items['espresso']['cost']}\nLatte ${menu_items['latte']['cost']}\nCappuccino ${menu_items['espresso']['cost']}:")
    return input(f"Which item would you like?").strip().lower()

# checks to make sure the item selected is available, and then that there is enough resources
def check_resources(menu_items, choice):
    if choice in menu_items:
        if((supplies["water"] >= menu_items[choice]['ingredients'].get('water', 0)) and
           (supplies['milk'] >= menu_items[choice]['ingredients'].get('milk', 0)) and
           (supplies['coffee'] >= menu_items[choice]['ingredients'].get('coffee', 0))):
            return True
    else:
        return print("Item Not Found")

# function to get money from user for selected item, give them change, and update profit
def cashier(menu_items, choice, profit):
    the_cost = menu_items[choice]['cost']
    print(f"The cost is {the_cost}")
    pennies = int(input("Enter number of Pennies: ")) * .01
    nickels = int(input("Enter number of Nickels: ")) * .05
    dimes = int(input("Enter number of Dimes: ")) * .1
    quarters = int(input("Enter number of Quarters: ")) * .25
    money = pennies + nickels + dimes + quarters
    
    if money >= the_cost:
        change = money - the_cost
        profit += the_cost
        print("Thank you, your change is " + str(change))
        return profit, True
    else:
        print("Sorry not enough money")
        return profit, False

def espresso_machine(menu_items, choice):
    ingredients = menu_items[choice]['ingredients']
    for items, amount in ingredients.items():
        supplies[items] -= amount
    print(f"Here is your {choice}. Please enjoy!")

while is_on == True:
    choice = selection(menu_items)
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {supplies['water']}\nMilk: {supplies['milk']}\nCoffee: {supplies['coffee']}\nProfit: {profit}")
    elif choice in menu_items:
        if check_resources(menu_items, choice):
            print("There is enough ingredients")
            profit, transaction = cashier(menu_items, choice, profit)
            if transaction:
                espresso_machine(menu_items, choice)
                print(f"Your profit is ${profit}")
        else:
            print("There isn't enough ingredients")
    else:
        print(f"Selection {choice} unknown. Please select from available options")