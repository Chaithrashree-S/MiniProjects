import random

def choose_word():
    words = ['apple', 'banana', 'orange', 'grape', 'strawberry']
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    return display

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print("Try to guess the word.")

    while True:
        print(display_word(word, guessed_letters))
        print(f"Attempts left: {attempts}")
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts -= 1
            print("Incorrect guess.")

            if attempts == 0:
                print("You ran out of attempts. Game over!")
                print(f"The word was: {word}")
                break
        else:
            print("Correct guess!")

            if all(letter in guessed_letters for letter in word):
                print("Congratulations! You've guessed the word!")
                break

# Call the function to play the game
hangman()
