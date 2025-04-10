import higherlowerart as hla
import random
from game_data import data
from os import system

# # Name, Follower Count, Description, Country
random.shuffle(data)

current_wrong = 0
max_wrong = 5
score = 0

def check_guess(guess, current_item, next_item):
    if guess == "a":
        return current_item['follower_count'] > next_item['follower_count']
    elif guess == "b":
        return current_item['follower_count'] <  next_item['follower_count']
    else:
        print(f"Something went wrong {current_item}\n{next_item}")
        return False
    
def check_answer(answer, current_item, next_item, score, current_wrong):
    if answer:
        score += 1
        print(f"Correct {current_item['name']} has {current_item['follower_count']} followers and {next_item['name']} has {next_item['follower_count']}")
    else:
        current_wrong += 1
        print(f"Wrong {current_item['name']} has {current_item['follower_count']} and {next_item['name']} has {next_item['follower_count']}")
    print(f"Score: {score}\nWrong: {current_wrong}\n")
    return score, current_wrong

def user_input(current_item, next_item):
    print(f"Who has more followers:\nOption a)\n{current_item['name']} with {current_item['follower_count']} who is a {current_item['description']} from {current_item['country']}")
    print(hla.versus)
    print(f"Option b)\n{next_item['name']} who is a {next_item['description']} from {next_item['country']}")

def game():
    score = 0
    current_wrong = 0
    for i in range(len(data) - 1):
        current_item = data[i]
        next_item = data[i + 1]
    
        print(hla.logo)
    
        user_input(current_item, next_item)
        guess = input("Choose 'a' or 'b': ").strip().lower()

        answer = check_guess(guess, current_item, next_item)

        score, current_wrong = check_answer(answer, current_item, next_item, score, current_wrong)
    
        if current_wrong == max_wrong:
            print("You lose!")
            break

game()