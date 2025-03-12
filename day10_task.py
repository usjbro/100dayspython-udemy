# Functions with outputs
# def my_function():
#     return 3 * 2

# output = my_function()

# def format_name(f_name, l_name):
#     return f_name.title(), l_name.title()

# formated_name = format_name("asdf","aslHJ")

# print(type(formated_name))
# print(formated_name[0] + " " + formated_name[1])

def is_leap_year(year):
    return (year % 4 == 0 and year % 400 != 0) or year % 100 == 0

year = int(input("Leap Year Checker: "))

if is_leap_year(year):
    print("Leap Year!")
else:
    print("Not a Leap Year")