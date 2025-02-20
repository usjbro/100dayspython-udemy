import random

from hangman_words import word_list
from hangman_art import stages
from hangman_art import logo

lives = 6

choosen_word = random.choice(word_list)
print(choosen_word)

place_holder = ""
word_length = len(choosen_word)

print(logo)

for position in range(word_length):
    place_holder += "_"
print(f"Word to guess: {place_holder}")

# 1

game_over = False
correct_letters = []


while not game_over:
    guess = input("Guess a letter: ").lower()

    display = ""

    for letter in choosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)
    print(correct_letters)

    if guess not in choosen_word:
        lives -= 1
        print(f"You have {lives} left")
        if lives == 0:
            game_over = 0
            print("You Suck")

    if "_" not in display:
        print("You Win!")
        game_over = True
# 2
    print(stages[lives])



