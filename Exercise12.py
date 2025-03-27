def first_last():
    a = []

    n = int(input("Enter the number of elements: "))

    for i in range(n):
        element = input(f"Enter element {i+1}: ")
        a.append(element)
    if a:
        print(f"The first element of the given list: {a[0]}")
        print(f"The last element of the given list: {a[-1]}")
    else:
        print("The list is empty")

first_last()


