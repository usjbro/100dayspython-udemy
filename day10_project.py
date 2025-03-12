print("Calculator")

first_num = float(input("First number: "))
second_num = float(input("Second number: "))
operation = input("Pick an operation:\n+\n-\n*\n/\n")
if operation == "+":
    print(f"The {first_num} + the {second_num} = ", first_num + second_num)
elif operation == "-":
    print(f"The {first_num} - the {second_num} = ", first_num - second_num)
elif operation == "*":
    print(f"The {first_num} * the {second_num} = ", first_num * second_num)
elif operation == "/":
    print(f"The {first_num} / the {second_num} = ", first_num / second_num)
else:
    print("Invalid operator entered")