import random  
choices = list(range(1, 10))

while True:
    player_choice = input("Choose a number (1-9) or type 'exit' to quit: ").strip()

    if player_choice.lower() == "exit":
        print("Bye!")
        break

    if not player_choice.isdigit():
        print("Invalid input! Please enter a number between 1 and 9.")
        continue

    player_choice = int(player_choice)

    if player_choice not in choices:
        print("Invalid number! Choose between 1 and 9.")
        continue

    computer_choice = random.choice(choices)
    
    result = "It's exactly right!" if player_choice == computer_choice else \
             "Too low!" if player_choice < computer_choice else "Too high!"
    
    print(result)

    