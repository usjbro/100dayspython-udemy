print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? "))
tip = float(input("How much do you want to tip? 10, 12, or 15 "))
people = int(input("How many people to split the bill? "))

total_bill = (tip / 100 * bill + bill) / people
rounded_bill = round(total_bill, 2)

## print(bill)
## print(tip)

print(f"Each person owes: ${rounded_bill}")
## print(f"Each person should pay {bill_per}")