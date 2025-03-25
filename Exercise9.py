import random

while True:
    player_choice = input("Choose a number (1-9) or type 'exit' to quit: ").strip().lower()

    if player_choice == "exit":
        print("Bye!")
        break

    try:
        player_choice = int(player_choice)
        if not (1 <= player_choice <= 9):
            raise ValueError  
    except ValueError:
        print("⚠️ Invalid input! Please enter a number between 1 and 9.")
        continue

    computer_choice = random.randint(1, 9) 
    print(f"Computer chose: {computer_choice}")

    result = "🎯 It's exactly right!" if player_choice == computer_choice else \
             "⬆️ Too low!" if player_choice < computer_choice else "⬇️ Too high!"

    print(result)