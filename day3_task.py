print("Welcome to the rollercoaster!")
height_in = float(input("What is your height in in? "))

height_cm = height_in * 2.54
bill = 0

if height_cm >= 120:
    print(f"You are {height_cm} cm tall and can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Please pay $5")
    elif age <= 18:
        bill = 7
        print("Please pay $7")
    else:
        bill = 12
        print("Please pay $12")
    
    wants_photo = input("Do you want a photo? y for yes or n for no: ")
    if wants_photo == "y":
        bill = bill + 3
        # Adds $3 to total bill
    print(f"Your final bill is {bill}.")
else:
    print(f"Sorry you have to grow taller before you can ride. height is {height_cm}")

# # divisor  = int(input("Divisor: "))
# # dividend = int(input("Dividend: "))
# # quotient = dividend / divisor
# # modulo = dividend % divisor
# # if modulo == 0:
# #     print(f"Quotient = {quotient}")
# #     print("Divisable")
# # else:
# #     print(f"Not divisable as quotient = {quotient} and remainder = {modulo}")

print("Welcome to Python Pizza deliveries!")
size = input("What size pizza do you want? S, M, L: ").upper()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()
extra_cheese = input("Do you want extra cheese? Y or N: ").upper()
bill = 0

# todo: work out how uch they need to pay based on their size choice
# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# elif size == "L":
#     bill += 25
# else:
#     print(f"Invalid input for pizza size: {size}")

# # todo: work out how much to add to their bill based on their pepperoni choice.
# if (pepperoni == "Y" and size == "S"):
#     bill += 2
# elif (pepperoni == "Y" and (size == "M" or size == "L")):
#     bill += 3
# elif pepperoni == "N":
#     bill += 0
# else:
#     print(f"Invalid input for pepperoni: {pepperoni}")

# # todo: work out their final amount based on wheter if the want extra cheese.
# if extra_cheese == "Y":
#     bill +=1
# elif extra_cheese == "N":
#     bill += 0
# else:
#     print(f"Invalid input for extra cheese: {extra_cheese}")

# print(f"Your total bill is {bill}")