import random

print("Welcome to the PyPassword Generator")
letters = ['a', 'b','c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

num_letters = int(input("How many letters would you like in your password?\n"))
num_numbers = int(input("How many numbers would you like in your password?\n"))
num_spec_char = int(input("How many special characters would you like in your password?\n"))

easy_password = ""

for number in range(0, num_letters):
    easy_password += letters[number]

for number in range(0, num_numbers):    
    easy_password += numbers[number]

for number in range(0, num_spec_char):
    easy_password += symbols[number]

print(f"Your easy password is {easy_password}")

complex_password = []

for char in range(num_letters):
    complex_password.append(random.choice(letters))
    # print(complex_password)
for char in range(num_numbers):
    complex_password.append(random.choice(numbers))
    # print(complex_password)
for char in range(num_spec_char):
    complex_password.append(random.choice(symbols))
    # print(complex_password)

random.shuffle(complex_password)
password = ""
for p in complex_password:
    password += p
print(f"Your complex password is {password}")