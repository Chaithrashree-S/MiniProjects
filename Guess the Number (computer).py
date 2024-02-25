import random

def computer_guess_number():
    low = 1
    high = 100
    attempts = 0

    print("Think of a number between 1 and 100, and I'll try to guess it.")

    while True:
        # Generate a guess by the computer
        guess = random.randint(low, high)
        print(f"My guess is: {guess}")
        feedback = input("Is my guess too high (H), too low (L), or correct (C)? ").upper()
        attempts += 1

        # Check the feedback and adjust the range for the next guess
        if feedback == "C":
            print(f"I guessed the number in {attempts} attempts!")
            break
        elif feedback == "H":
            high = guess - 1
        elif feedback == "L":
            low = guess + 1
        else:
            print("Please enter H, L, or C.")

# Call the function to let the computer guess the number
computer_guess_number()
