import random  
import string

def game():
    #create random 4 numbers
    characters = string.digits
    secret_num = "".join(random.choice(characters) for _ in range(4))  

    print("Welcome to the Cows and Bulls Game!")

    while True:
        user_num = input("Enter a 4-digit number (or 'exit' to quit): ").strip()
        
        if user_num.lower() == "exit":
            print(f"The secret number was: {secret_num}")
            break
        if not user_num.isdigit() or len(user_num) != 4:
            print("Invalid input! Enter exactly 4 digits.")
            continue

        #Calculating the number of cows and bulls
        cows = sum(1 for i in range(4) if user_num[i] == secret_num[i])
        bulls = sum(1 for digit in user_num if digit in secret_num) - cows

        print(f"Cows: {cows}, Bulls: {bulls}")
        if cows == 4:
            print("Congrats! You guessed the number correctly.")
            break

game()

