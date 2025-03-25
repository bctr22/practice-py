import random

def get_winner(player, computer):
    if player == computer:
        return "It's a Draw!"
    rules = {
        "rock": "scissors",  # Rock beats Scissors
        "paper": "rock",     # Paper beats Rock
        "scissors": "paper"  # Scissors beats Paper
    }
    return "You won! 🎉" if rules[player] == computer else "You lost! 😢"

def play_game():
    choices = ["rock", "paper", "scissors"]
    
    while True:
        player_choice = input("Choose Rock, Paper, or Scissors (or 'quit' to exit): ").lower()
        
        if player_choice == "quit":
            print("Thanks for playing! 👋")
            break

        if player_choice not in choices:
            print("Invalid choice! Please enter rock, paper, or scissors.")
            continue
        
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        result = get_winner(player_choice, computer_choice)
        print(result)

# Run game
if __name__ == "__main__":
    play_game()
