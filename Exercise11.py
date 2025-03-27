def is_Prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0 :
            return False
    return True


def get_num():
   while True:
        try:
            return int(input("Give me a number: "))
        except ValueError:
            print("Invalid input! Please enter a valid integer.")


a = get_num()
print(f"{a} is prime: {is_Prime(a)}")