x = int(input('pls input number: '))

if x % 2 == 0:  
    print(f'{x} is even')
else:
    print(f'{x} is odd')

#extra
#1
if x % 4 == 0:
    print(f'{x} is divisible by 4')
#2
check = int(input('pls input number one: '))
num = int(input('pls input number two: '))
if check % num == 0:
    print(f'{check} is divisible by {num}')
else:
    print('no')