a = [1, 1, 2, 2, 3, 4, 5, 6, 8, 21, 13, 3, 5, 8, 13, 21, 34, 55, 89]

#using loop
def filter():
    b = []
    for _ in a:
        if _ not in b:
            b.append(_)
    return b

#using sets
a = list(set(a))

#rel
print(filter())

print(a)