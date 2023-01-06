import os
from art import logo

bidders = []
bidding_finished = False

print(logo)
print("Welcome to the secret auction program.")


def find_highest_bidder():
    winner = ''
    highest = 0
    for bidder in bidders:
        if bidder['bid'] > highest:
            winner = bidder['name']
            highest = bidder['bid']
    print(f"The winner is {winner} with the bid of ${highest}.")


while not bidding_finished:
    person = {}
    name = input("What is your name? ")
    bid = int(input("What's your bid? $"))
    person['name'] = name
    person['bid'] = bid
    bidders.append(person)
    answer = input("Are there any other bidders? Type 'yes'or 'no. ").lower()
    if answer == 'no':
        bidding_finished = True
        find_highest_bidder()
    elif answer == 'yes':
        os.system("cls")
