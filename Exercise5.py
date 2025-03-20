import random
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

common = list(set(a) & set(b))
print(common)

#1
c = random.sample(range(1,100), 10)
d = random.sample(range(1,100), 5)
new_common = list(set(c) & set(d))
print(f"List C: {c}")
print(f"List D: {d}")
print(f"Common elements: {new_common}")

#2
print(set(a) & set(b))
