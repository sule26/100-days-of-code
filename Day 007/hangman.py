import random
import os
from hangman_art import logo, stages
from hangman_words import word_list

lives = 6
end_of_game = False

chosen_word = random.choice(word_list)
display = []
for i in range(len(chosen_word)):
    display.append("_")


print(logo)
print(f"pssst, the solution is {chosen_word}.")

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    os.system("cls")

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:
            display[position] = guess

    if guess not in chosen_word:
        print(f"you guessed {guess}, that's not in the word. You lose a life")
        lives -= 1
        if lives == 0:
            print("You lose")
            end_of_game = True

    print(stages[lives])
    print(f"{' '.join(display)}")

    if "_" not in display:
        print("You win!")
        end_of_game = True

print("Game Over!")
