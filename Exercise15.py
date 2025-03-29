def rev():
    a = input("type anything: ")
    return " ".join(a.split()[::-1])

print(rev())