x = int(input('enter number: '))
y = range(1,x + 1)
for num in y:
    if x % num == 0:
        print(num)