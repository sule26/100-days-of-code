import random
import os
from art import logo

is_game_over = False

def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards_in_hand):
    if len(cards_in_hand) == 2 and sum(cards_in_hand) == 21:
        return 0
    if 11 in cards_in_hand and sum(cards_in_hand) > 21:
        cards_in_hand.remove(11)
        cards_in_hand.append(1)
        return sum(cards_in_hand)
    return sum(cards_in_hand)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw! 🙃"
    elif computer_score == 0:
        computer_score == 21
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        user_score == 21
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return 'You win 😃'
    else:
        return 'You lose 😤'


def blackjack():
    print(logo)

    user_cards = []
    computer_cards = []
    is_game_over = False

    for i in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"    Your cards: {user_cards}, current score: {sum(user_cards)}")
        print(f"    Computer's first card: {computer_cards[0]}")
        
        if user_score == 0 or user_score > 21 or computer_score == 0:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_should_deal == 'y':
                user_cards.append(deal_cards())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)

    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Computer's final hand: {computer_cards}, final score {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of BlackJack? Type 'y' or 'n': ").lower() == 'y':
    os.system('cls')
    blackjack()
