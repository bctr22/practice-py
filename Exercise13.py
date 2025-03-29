def fibonacci():
    n = int(input("put a number in lil bro: "))

    if n < 0:
        print("wtf bro?")
        return []

    fib_list = [0, 1]

    for _ in range (2, n):
        fib_list.append(fib_list[-1] + fib_list[-2])

    return fib_list[:n]

print(fibonacci())
