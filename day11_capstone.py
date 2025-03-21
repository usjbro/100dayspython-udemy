import random
import art

print(art.logo)

def deal_card():
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    card = random.choice(cards)
    return card

def calc_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)

def determine_winner(player_score, dealer_score):
    print("\nFinal Results:")
    print(f"Player's final score: {player_score}")
    print(f"Dealer's final score: {dealer_score}")

    if player_score > 21:
        print("Player busts! Dealer wins.")
        is_game_over = True
    elif dealer_score > 21:
        print("Dealer busts! Player wins.")
        is_game_over = True
    elif player_score == dealer_score:
        print("It's a draw!")
        is_game_over = True
    elif player_score == 21:
        print("Player wins with a Blackjack!")
        is_game_over = True
    elif dealer_score == 21:
        print("Dealer wins with a Blackjack!")
        is_game_over = True
    elif player_score > dealer_score:
        print("Player wins!")
        is_game_over = True
    else:
        print("Dealer wins!")

player_cards = []
dealer_cards = []
computer_score = -1
player_score = -1
is_game_over = False

for _ in range(2):
    player_cards.append(deal_card())
    dealer_cards.append(deal_card())

while not is_game_over:
    player_score = calc_score(player_cards)
    dealer_score = calc_score(dealer_cards)

    print(f"Your cards are: {player_cards}, current score: {player_score}")
    print(f"Dealers first card is {dealer_cards[0]}")
    # print(f"Dealers cards: {dealer_cards}") #Debug show dealers cards


    if player_score == 0 or dealer_score == 0 or player_score > 21:
        is_game_over = True
    else:
        player_continue = input("Do you hand to (h)it or (s)tand? ")
        if player_continue == "h":
            player_cards.append(deal_card())
            player_score = calc_score(player_cards)
        else:
            is_game_over = True

while dealer_score != 0 and dealer_score < 17:
    dealer_cards.append(deal_card())
    dealer_score = calc_score(dealer_cards)

print(determine_winner(player_score, dealer_score))