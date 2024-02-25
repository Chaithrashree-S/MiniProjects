import random

def play_game():
    options = ['rock', 'paper', 'scissors']

    while True:
        # Get user's choice
        user_choice = input("Enter rock, paper, or scissors (or 'q' to quit): ").lower()

        if user_choice == 'q':
            print("Thanks for playing!")
            break

        if user_choice not in options:
            print("Invalid choice. Please enter rock, paper, or scissors.")
            continue

        # Computer's choice
        computer_choice = random.choice(options)

        print(f"Computer chooses: {computer_choice}")

        # Determine the winner
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            print("You win!")
        else:
            print("Computer wins!")

# Call the function to play the game
play_game()
