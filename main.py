import random

word_list = ["aardvark", "baboon", "camel"]

print("Welcome to the HANGMAN game\n")

chosen_word = random.choice(word_list)

lives = 10
victory = False

hint = ""

for n in range(len(chosen_word)):
    hint += "_"


while lives > 0 and victory is False:
    print(chosen_word)
    print(hint)
    print(lives)

    guess = input("Guess a letter\n").lower()

    if len(guess) > 1:
        lives -= 1
        continue

