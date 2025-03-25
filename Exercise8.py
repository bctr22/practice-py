import random

choices = ["rock", "paper", "scissors"]

while True:
    x = input("Rock-Paper-Scissors (or 'quit' to exit): ").lower()

    if x == "quit":
        print("Game over. Thanks for playing!")
        break

    if x not in choices:
        print("Invalid input! Please enter rock, paper, or scissors.")
        continue  

    y = random.choice(choices)
    print(f"Computer chose: {y}")

    if x == y:
        print("Draw")
    elif (x == "rock" and y == "scissors") or (x == "paper" and y == "rock") or (x == "scissors" and y == "paper"):
        print("You won!")
    else:
        print("You lost!")
