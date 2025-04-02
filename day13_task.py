# def my_func():
#     for i in range(1, 21):
#         if i == 20:
#             print("You got it")

# my_func()

# # Describe the Problem - Write your answers as comments:
# # 1. What is the for loop doing?
# # The loop is starting at 1 and going to 19 assigning the number to i
# # 2. When is the function meant to print "You got it"?
# # The function prints You got it when i is equal to 20
# # 3. What are your assumptions about the value of i?
# # i starts at 1 and stops at 19

# from random import randint
# dice_images = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]
# dice_num = randint(0, 5)
# print(dice_images[dice_num])

# year = int(input("What's your year of birth?"))

# if year > 1980 and year < 1994:
#     print("You are a millennial.")
# #elif year > 1994:
# elif year >= 1994:
#     print("You are a Gen Z")

# try:
#     age = int(input("How old are you?"))
# except ValueError:
#     print("Only integers please!")
#     age = int(input("How old are you?"))

# if age > 18:
#     print(f"You can drive at age {age}")
# else:
#     print(f"You can't drive at age {age}")

# word_per_page = 0
# pages = int(input("Number of pages: "))
# #word_per_page == int(input("Number of words per page: ")) should be 1 = not 2 =
# word_per_page = int(input("Number of words per page: "))
# total = words = pages * word_per_page

# print(f"pages = {pages}")
# print(f"words_per_page = {word_per_page}")
# print(f"total words: {total}")

import random
import maths

def mutate(a_list):
    b_list = [
    ]
    new_item = 0

    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item = maths.add(new_item, item)
        b_list.append(new_item)
    print(b_list)

mutate([1, 2, 3, 5, 8, 13])