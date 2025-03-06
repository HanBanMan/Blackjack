import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def blackjack():
    user_cards = []
    computer_cards = []
    another_card = True
    print(art.logo)
    user_cards.append(random.choice(cards)) #Add a card to user deck
    computer_cards.append(random.choice(cards)) #Add a card to computer deck
    another_card = "y"
    while another_card == "y": # User cards
        user_cards.append(random.choice(cards))
        user_score = sum(user_cards)
        print(f"    Your cards: {user_cards}, current score: {user_score}")
        print(f"    Computers first card: {computer_cards}")
        if user_score <= 21:
            if user_score == 21:
                print("Win with a Blackjack! 🤑")
                return
            elif user_score < 21:
                another_card = input("type \"y\" to get another card, type \"n\" to pass:")
        elif user_score == 21: # Win Blackjack
            print("Win with a Blackjack! 🤑")
            return
        else: # Loose for being over 21
            if 11 in user_cards and user_score > 21:
                user_score -= 10
            else:
                print("You went over. You lose! 🥴")
                return
    else:
        user_score = sum(user_cards)
        print(f"  Your final hand: {user_cards}, current score: {user_score}")
        # Dealing cards to computer
        while sum(computer_cards) <= 17:
            computer_cards.append(random.choice(cards))
        else:
            if sum(computer_cards) > 17:
                print(f"  Computer final hand: {computer_cards}, final score: {sum(computer_cards)}")
            # Printing Final Outcome
            if sum(computer_cards) < user_score or sum(computer_cards) > 21: # Your cards are closer to 21
                print("You win 🥳")
            elif sum(computer_cards) == user_score: # Draw Outcome
                print("Draw 😑")
            elif sum(computer_cards) == 21: #Computer Blackjack
                print("You lose. Computer has Blackjack 😭")

play_game = "y"
while play_game == "y":
    play_game = input("Do you want to play a game of Blackjack?  Type \"y\" or \"n\": ")
    blackjack()
else:
    print("Bye!")

