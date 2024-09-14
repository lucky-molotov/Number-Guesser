import random

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
        print(f"Number of attempts remaining: {attempts}")
        try:
            guessed_number = int(input("Guess the Number (0 to 10): "))
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 10.")
            continue

        if guessed_number == random_number:
            print(f"Congratulations! You guessed correctly with {3 - attempts} attempts used.")
            human_wins += 1  # Increment human win
            break
        else:
            attempts -= 1
            print("Incorrect, try again.")
    
    if attempts == 0:
        print(f"Sorry, you've run out of attempts. The correct number was {random_number}.")
        human_losses += 1  # Increment human loss

def pc_vs_human():
    global pc_wins, pc_losses
    try:
        number_to_be_guessed = int(input("Input a number for the computer to guess (0 to 10): "))
        if not 0 <= number_to_be_guessed <= 10:
            raise ValueError
    except ValueError:
        print("Invalid input. Please enter a number between 0 and 10.")
        return
    
    attempts = 3
    while attempts > 0:
        guessed_number = random.randint(0, 10)
        print(f"Computer guesses: {guessed_number}")

        if guessed_number == number_to_be_guessed:
            print(f"The computer guessed correctly! It used {3 - attempts} attempts.")
            pc_wins += 1  # Increment PC win
            break
        else:
            attempts -= 1
            print(f"Incorrect guess. Attempts remaining: {attempts}")
    
    if attempts == 0:
        print("Congratulations! The computer couldn't guess your number.")
        pc_losses += 1  # Increment PC loss

def display_stats():
    """Displays the win/loss record for both human and PC."""
    print("\n--- Game Stats ---")
    print(f"Human Wins: {human_wins}, Human Losses: {human_losses}")
    print(f"PC Wins: {pc_wins}, PC Losses: {pc_losses}")
    print("-------------------\n")

def menu():
    while True:
        print("""
        Number Guessing Game
        Select an Option:
        1: Human vs PC
        2: PC vs Human
        3: Display Win/Loss Record
        4: Exit
        """)
        try:
            choice = int(input("Choose an option (1-4): "))
            if choice == 1:
                human_vs_pc()
            elif choice == 2:
                pc_vs_human()
            elif choice == 3:
                display_stats()
            elif choice == 4:
                print("Exiting the game. Goodbye!")
                break
            else:
                print("Invalid choice, please choose 1, 2, 3, or 4.")
        except ValueError:
            print("Invalid input, please enter a number (1-4).")

menu()
