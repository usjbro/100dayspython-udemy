print("Calculator")

def add(first_num, second_num):
    return first_num + second_num
    # result = first_num + second_num
    # print(f"The {first_num} + the {second_num} = {result}")


def subtract(first_num, second_num):
    return first_num - second_num
    # result = first_num - second_num
    # print(f"The {first_num} - the {second_num} = {result}")


def multi(first_num, second_num):
    return first_num * second_num
    # result = first_num * second_num
    # print(f"The {first_num} * the {second_num} = {result}")


def divide(first_num, second_num):
    return first_num / second_num
    # result = first_num / second_num
    # print(f"The {first_num} / the {second_num} = {result}")


operations = {"+": add, "-": subtract, "*": multi, "/": divide}

choice = "n"
while choice != "q":
    if choice == "n":
        first_num = float(input("First number: "))
    second_num = float(input("Second number: "))
    operation = input("Pick an operation:\n+\n-\n*\n/\n")
    if operation in operations:
        answer = operations[operation](first_num, second_num)
        print(first_num, operation, second_num, " = ", str(answer))
        choice = input(print(f"(y) to contine with {answer} or (n) to pick new first number or (q) to quit"))
        if choice == "y":
            print(f"First number: {answer}")
            first_num = answer
    else:
        print("Unknown operation")
