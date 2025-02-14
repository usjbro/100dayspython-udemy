import random

options = ["Rock", "Paper", "Scissors"]
selection = int(input("What do you choose? Type 0 for rock, 1 for Paper, 2 for Scissors"))

print(options[selection])
comp_selection = random.choice(options)
index = options.index(comp_selection)

if index == 0: # computer Rock
    if selection == 0: # computer Rock user Rock
        print(f"Draw: User: {options[selection]}, Computer: {comp_selection}")
    elif selection == 1: # computer Rock user Paper
        print(f"User wins with {options[selection]} and computer {comp_selection}")
    else: # computer Rock user Scissors
        print(f"User looses with {options[selection]} and computer wins with {comp_selection}")
elif index == 1: # computer Paper
    if selection == 0: # computer Paper user Rock
        print(f"User looses with {options[selection]} and computer wins with {comp_selection}")
    elif selection == 1: # computer Paper user Paper
        print(f"Draw: User: {options[selection]}, Computer: {comp_selection}")
    else: # computer Paper user Scissors
        print(f"User wins with {options[selection]} and computer looses with {comp_selection}")
else: # computer Scissors
    if selection == 0: # computer Scissors user Rock
        print(f"User wins with {options[selection]} and computer looses with {comp_selection}")
    elif selection == 1: # computer Scissors user Paper
        print(f"User looses with {options[selection]} and computer wins with {comp_selection}")
    else: # computer Scissors user Scissors
        print(f"Draw: User: {options[selection]}, Computer: {comp_selection}")
