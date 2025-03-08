# # # # dictionary
# # # programming_dictionary = {
# # #     "Bug": "An error in a program that prevents the program from running as expected.",
# # #     "Function": "A piece of code that you can easily call over and over again.",
# # #     "Loop": "The action of doing something over and over again."
# # # }

# # # # prints the values
# # # for key in programming_dictionary.values():
# # #     print(key)

# # # # prints the key
# # # for key in programming_dictionary:
# # #     print(key)
# # #     # prints the value
# # #     print(programming_dictionary[key])

# # # empty_dictionary = {}

# # # student_grade = {}
# # # student_grade.

# # # # wipe an existing dictionary

# # # # programming_dictionary = {}
# # # # print(programming_dictionary)

# # # # Edit an item in a dictionary
# # # programming_dictionary["Bug"] = "A moth in your computer"
# # # print(programming_dictionary)

# student_scores = {
#     'Harry': 88,
#     'Ron': 78,
#     'Hermione': 95,
#     'Draco': 75,
#     'Neville': 60
# }

# student_grades = {}

# for student, score in student_scores.items():
#     if 91 <= score <= 100:
#         student_grades[student] = "Outstanding"

#     elif 81 <= score <= 90:
#         student_grades[student] = "Exceeds Expectations"

#     elif 71 <= score <= 80:
#         student_grades[student] = "Acceptable"

#     else:
#         student_grades[student] = "Fail"

# print(student_grades)

# Nesting

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Stuttgart", "Berlin"] 
# }

# Print Lille
# print(travel_log["France"][1])

# nested_list = ["A", "B", ["C", "D"]]
# print(nested_list[2][1])

travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgard"],
        "total_visits": 5
    },
}
print(travel_log["Germany"]["cities_visited"][2])