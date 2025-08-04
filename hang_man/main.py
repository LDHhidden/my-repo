import random
import hangman_words
from hangman_arts import logo
from hangman_arts import stages

print(logo)
lives = 6
chioce_word = random.choice(hangman_words.word_list)
print(chioce_word)

blank_word = ""

for letter in chioce_word:
    blank_word += "_"
print(blank_word)

game_over = False
confirm_letter = []

while game_over == False:
    chioce_letter = input("guess: \n")
    display_word = ""

    if chioce_letter in confirm_letter:
        print("이미 했던 알파벳입니다.")

    for letter in chioce_word:
        if letter == chioce_letter:
            display_word += chioce_letter
            confirm_letter.append(chioce_letter)
        elif letter in confirm_letter:
            display_word += letter
        else:
            display_word += "_"
            
    print(display_word)

    if chioce_letter in confirm_letter:
        print(stages[lives])
    else:
        print(stages[lives-1])
        lives -= 1

    if lives == 0:
        game_over = True
        print("hangman die!")

    if "_" not in display_word:
        game_over = True
        print("hangman live!")