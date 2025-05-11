import random

def play_round():
    valid_choices = ["rock", "paper", "scissors"]
    while True:
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if user_choice in valid_choices:
            break
        else:
            print("Invalid choice. Please try again.")
    computer_choice = random.choice(["rock", "paper", "scissors"])
    print(f"Computer chose: {computer_choice}.")

    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):   
        return "You win!"
    else:
        return "Computer win!"


def game():
    user_score = 0
    computer_score = 0

    while True:
        result = play_round()
        print(result)

        if "You win" in result:
            user_score += 1
        elif "Computer win" in result:
            computer_score += 1

        print(f"Score - User: {user_score}, Computer: {computer_score}")

        continue_check = ["y","n"]
        while True:
            continue_check = input("Do you want to play again? (y/n): ").lower()
            if continue_check in ['y', 'n']:
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
        if continue_check == 'n':
            print("Thanks for playing!")
            break

        
        if continue_check != 'y':
            print("Thanks for playing!")
            break
# Start the game
game()
