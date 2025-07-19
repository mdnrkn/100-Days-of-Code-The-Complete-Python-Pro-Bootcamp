import random
from wordList import word_list

print("Welcome to Guessing Game!")
lives = 5
chosen_word = random.choice(word_list).lower()

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_ "
print(placeholder)

game_over = False
correct_letters = []

while not game_over:

    print(f"You've {lives}/5 lives left.")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}.")

    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)

        elif letter in correct_letters:
            display += letter    

        else:
            display += "_ "

    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You've guess {guess}, that's not in the word. You lose a life.")

        if lives == 0:
            print("You lose! The word was:", chosen_word)
            game_over = True

    if "_" not in display:
        print("You've guessed the word!")
        game_over = True