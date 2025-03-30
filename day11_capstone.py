import random
import art

def deal_card():
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    return random.choice(cards)

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
        return("Player busts! Dealer wins.")
    elif dealer_score > 21:
        return("Dealer busts! Player wins.")
    elif player_score == dealer_score:
        return("It's a draw!")
    elif player_score == 21:
        return("Player wins with a Blackjack!")
    elif dealer_score == 21:
        return("Dealer wins with a Blackjack!")
    elif player_score > dealer_score:
        return("Player wins!")
    else:
        print("Dealer wins!")

def play_game():
    player_cards = [deal_card(), deal_card()]
    dealer_cards = [deal_card(), deal_card()]

    is_game_over = False

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
            else:
                is_game_over = True

    while calc_score(dealer_cards) < 17:
        dealer_cards.append(deal_card())

    dealer_score = calc_score(dealer_cards)
    print(determine_winner(player_score, dealer_score))

while input("Do you want to play blackjack (y)yes or (n)no? ").lower() == "y":
    print("\n"* 20)
    print(art.logo)
    play_game()