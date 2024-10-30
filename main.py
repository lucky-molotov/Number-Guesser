import random,time

# Global variables to track wins and losses
human_wins = 0
human_losses = 0
pc_wins = 0
pc_losses = 0

def human_vs_pc():
    global human_wins, human_losses
    random_number = random.randint(0, 10)
    attempts = 3
    while attempts > 0:
        print(f"Number of attempts remaining: {attempts}\n")
        try:
            guessed_number = int(input("Guess the Number (0 to 10): "))
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 10.\n")
            continue

        if guessed_number == random_number:
            print(f"Congratulations! You guessed correctly with {3 - attempts} attempts remaining.\n")
            human_wins += 1  # Increment human win
            break
        else:
            attempts -= 1
            print("Incorrect, try again.\n")
    
    if attempts == 0:
        print(f"Sorry, you've run out of attempts. The correct number was {random_number}.\n")
        human_losses += 1  # Increment human loss

def pc_vs_human():
    """The computer tries to guess a number chosen by the human player."""
    global pc_wins, pc_losses

    # Prompt the user for a number
    while True:
        try:
            number_to_guess = int(input("Input a number for the computer to guess (0 to 10): "))
            if 0 <= number_to_guess <= 10:
                break
            print("Invalid input. Please enter a number between 0 and 10.\n")
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 10.\n")

    # Set up the game loop
    attempts = 3
    while attempts > 0:
        computer_guess = random.randint(0, 10)
        print(f"Computer guesses: {computer_guess}\n")
        time.sleep(1)

        # Check if the computer guessed correctly
        if computer_guess == number_to_guess:
            print(f"The computer guessed correctly! It used {3 - attempts} attempts.\n")
            pc_wins += 1  # Increment PC win
            break
        else:
            attempts -= 1
            print(f"Incorrect guess. Attempts remaining: {attempts}\n")
    else:
        print("Congratulations! The computer couldn't guess your number.\n")
        pc_losses += 1  # Increment PC loss

def display_stats():
    """Display the win/loss record for both the human player and the computer."""
    print("\n--- Game Statistics ---")
    print(f"Human Wins: {human_wins}, Losses: {human_losses}")
    print(f"Computer Wins: {pc_wins}, Losses: {pc_losses}")
    print("-----------------------\n")
    time.sleep(2)
def menu():
    """Displays the main menu for the Number Guessing Game."""
    while True:
        print("\n")
        print("Number Guessing Game")
        print("--------------------")
        print("Select an Option:")
        print("1: Human vs PC")
        print("2: PC vs Human")
        print("3: Display Win/Loss Record")
        print("4: Exit")
        print("--------------------")
        
        try:
            option = int(input("Choose an option (1-4): "))
            if option == 1:
                human_vs_pc()
            elif option == 2:
                pc_vs_human()
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

