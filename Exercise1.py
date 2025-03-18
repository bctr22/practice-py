# Character Input
import datetime

today = datetime.datetime.now()

x = input('Enter your name: ')
y = int(input('Enter your age: '))
rel = today.year + 100 - y
message = f'Hi, {x}, you will be 100 years old in the year {rel}.'

print(message)

#extras
n = int(input('Enter a number: '))

#1 
print((message + " ") * n)

#2 
print((message + "\n") * n)