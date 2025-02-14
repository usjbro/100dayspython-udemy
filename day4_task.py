# import random

# # random_integer = random.randint(1, 10)
# # print(random_integer)

# random_number_0_to_1 = random.random() * 10
# print(random_number_0_to_1)

# if random_number_0_to_1 > 5:
#     print("Heads")
# else:
#     print("Tails")

# Lists
# states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
# states_of_america[1] = "Pencilvania"
# states_of_america.extend(["Angelaland", "Jack Bauer Land"])
# for x in states_of_america:
#     print(x, end="\n")
#  print(states_of_america[49])

# import random
# friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# # option 1
# print(random.choice(friends))

# # option 2
# random_index = random.randint(0, 4)
# print(friends[random_index])

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
 
print(dirty_dozen[1][1])