import random
import numberart as art

def initalize_game():
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard':").lower()
    if difficulty == 'easy':
        return 10
    elif difficulty == 'hard':
        return 5
    else:
        print("Invalid input. Defaulting to EXTREME MODE!!! HAHAHAHAHA! You have 1 attempt.")
        return 1

def make_guess():
    while True:
        try:
            return int(input("Guess a number: "))
        except ValueError:
            print("Invalid guess. Guess again")

def check(guess, answer):
    if guess > answer:
        print("Too high")
        return False
    elif guess < answer:
        print("Too Low")
        return False
    else:
        print(f"Yay you guessed the number: {answer}")
        return True

def game():
    initalize_game()
    answer = random.randrange(1, 100)
    attempts = set_difficulty()
    
    while attempts > 0:
        guess = make_guess()
        if check(guess, answer):
            return # User wins
        
        attempts -= 1

        if attempts > 0:
            print(f"You have {attempts} attempts remaining to guess the number")
        else:
            print(f"Sorry! You have run out of turns. the correct answer was {answer}")

game()