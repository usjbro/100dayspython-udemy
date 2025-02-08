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

# divisor  = int(input("Divisor: "))
# dividend = int(input("Dividend: "))
# quotient = dividend / divisor
# modulo = dividend % divisor
# if modulo == 0:
#     print(f"Quotient = {quotient}")
#     print("Divisable")
# else:
#     print(f"Not divisable as quotient = {quotient} and remainder = {modulo}")

