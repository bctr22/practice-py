a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for element in a:
    if element < 5: print(element)

#1
new_list = [num for num in a if num < 5]
print(new_list)

#2
print([num for num in a if num < 5])

#3
x = int(input("enter number: "))
print([num for num in a if num < x])
