import secrets
import string

def generate_password():
    while True:
        choice = input("1. Weak password\n2. Strong password\nType 'quit' to exit: ").strip()
        
        if choice.lower() == "quit":
            print("gud bye lil br")
            break
        
        if choice not in ("1", "2"):
            print("wtf bro, choose 1 or 2")
            continue
        
        pwd_length = 6 if choice == "1" else 13
        characters = string.digits if choice == "1" else string.ascii_letters + string.digits + string.punctuation
        
        password = "".join(secrets.choice(characters) for _ in range(pwd_length))
        print(f"Generated Password: {password}\n")

generate_password()
