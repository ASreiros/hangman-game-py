import random
import hangman_art

word_list = ["aardvark", "baboon", "camel"]

print(hangman_art.logo)
print("Welcome to the HANGMAN game\n")

chosen_word = random.choice(word_list).lower()

lives = 6
victory = False

hint = ""

for n in range(len(chosen_word)):
    hint += "_"


while lives > 0 and victory is False:
    print(hangman_art.stages[lives])
    print(hint)

    guess = input("Guess a letter\n").lower()

    if len(guess) > 1:
        print("You can guess only 1 letter")
        lives -= 1
        continue

    if chosen_word.count(guess) == 0:
        lives -= 1
        continue

    for n in range(len(chosen_word)):
        if chosen_word[n] == guess:
            hintList = list(hint)
            hintList[n] = guess
            hint = "".join(hintList)

    if chosen_word == hint:
        victory = True
        print("Congratulations!!! You won!!!")


if lives == 0:
    print(hangman_art.stages[lives])
    print("Game Over!!!You lost!!!")
