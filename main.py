import random,time
# Global variables to track wins and losses
human_wins = 0
human_losses = 0
pc_wins = 0
pc_losses = 0

def human_vs_computer():
    """The human player attempts to guess a randomly chosen number."""
    global human_wins, human_losses
    target_number = random.randint(0, 10)
    remaining_attempts = 3

    while remaining_attempts > 0:
        print(f"Attempts left: {remaining_attempts}\n")
        try:
            player_guess = int(input("Guess the number (0 to 10): "))
        except ValueError:
            print("Invalid input. Please enter a valid number between 0 and 10.\n")
            continue

        if player_guess == target_number:
            print(f"Congratulations! You guessed correctly with {remaining_attempts} attempts remaining.\n")
            human_wins += 1
            break
        else:
            remaining_attempts -= 1
            print("Incorrect guess, please try again.\n")
    
    if remaining_attempts == 0:
        print(f"Sorry, you've used all attempts. The correct number was {target_number}.\n")
        human_losses += 1

def computer_vs_human():
    """The computer tries to guess a number chosen by the human player."""
    global pc_wins, pc_losses

    # Prompt the user for a number
    while True:
        try:
            target_number = int(input("Input a number for the computer to guess (0 to 10): "))
            if 0 <= target_number <= 10:
                break
            print("Invalid input. Please enter a valid number between 0 and 10.\n")
        except ValueError:
            print("Invalid input. Please enter a valid number between 0 and 10.\n")

    # Set up the game loop
    attempts_remaining = 3
    while attempts_remaining > 0:
        computer_guess = random.randint(0, 10)
        print(f"Computer guesses: {computer_guess}")
        time.sleep(1)

        # Check if the computer guessed correctly
        if computer_guess == target_number:
            print(f"The computer guessed correctly! It used {3 - attempts_remaining} attempts.\n")
            pc_wins += 1  # Increment PC win
            break
        else:
            attempts_remaining -= 1
            print(f"Incorrect guess. Attempts remaining: {attempts_remaining}\n")
    else:
        print("Congratulations! The computer couldn't guess your number.\n")
        pc_losses += 1  # Increment PC loss

def display_stats():
    """Display the win/loss record for both the human player and the computer."""
    print(f"""
    --- Game Statistics ---
--Human Wins: {human_wins}, Losses: {human_losses}--
--Computer Wins: {pc_wins}, Losses: {pc_losses}--
    -----------------------
    """)
    time.sleep(2)
def menu():
    """Displays the main menu for the Number Guessing Game."""
    while True:
        print(f"""
        Number Guessing Game
        --------------------
        Select an Option
        1: Human vs PC
        2: PC vs Human
        3: Display Win/Loss Record
        4: Exit
        --------------------
        """)
        try:
            option = int(input("Choose an option (1-4): "))
            if option == 1:
                human_vs_computer()
            elif option == 2:
                computer_vs_human()
            elif option == 3:
                display_stats()
            elif option == 4:
                print("Exiting the game. Goodbye!")
                break
            else:
                print("Invalid choice, please choose 1, 2, 3, or 4.")
        except ValueError:
            print("Invalid input, please enter a number (1-4).")
         
menu()

