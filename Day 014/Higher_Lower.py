from art import logo, vs
from game_data import data
import random
import os


def get_random_account():
    return random.choice(data)


def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == 'A'
    else:
        return guess == 'B'


def higher_lower():
    score = 0
    is_correct = False
    is_game_over = False
    Account_B = get_random_account()

    print(logo)
    while not is_game_over:
        Account_A = Account_B
        Account_B = get_random_account()

        while Account_A == Account_B:
            Account_B = get_random_account()

        print(f"Compare A: {Account_A['name']}, a {Account_A['description']}, from {Account_A['country']}.")
        print(vs)
        print(f"Against B: {Account_B['name']}, a {Account_B['description']}, from {Account_B['country']}.")
        guess = input("Who has more followers? Type 'A' or 'B': ").upper()
        is_correct = check_answer(guess, Account_A['follower_count'], Account_B['follower_count'])

        os.system("cls")
        print(logo)
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            is_game_over = True
            print(f"Sorry, that's wrong. Final score: {score}.")

higher_lower()
