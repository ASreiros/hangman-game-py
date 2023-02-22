import random
import hangman_art
import hangman_words
import languages

print(hangman_art.logo)
print("Welcome to the HANGMAN game\n")

lang_check = False
language = 4

while lang_check is False:
    language = input("Choose a language. 0 for English, 1 for Lithuanian, 2 for Russian\n")
    if language == "0" or language == "1" or language == "2":
        lang_check = True
        language = int(language)



chosen_word = random.choice(hangman_words.word_list[language]).lower()
lives = 6
victory = False

hint = ""

for n in range(len(chosen_word)):
    hint += "_"


while lives > 0 and victory is False:
    print(chosen_word)
    print(hangman_art.stages[lives])
    print(hint)

    guess = input(languages.messages[language][0] + "\n").lower()

    if len(guess) > 1:
        print(languages.messages[language][1])
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
        print(languages.messages[language][2])


if lives == 0:
    print(hangman_art.stages[lives])
    print(languages.messages[language][3])
