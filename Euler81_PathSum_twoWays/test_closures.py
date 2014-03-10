def counter():
    count = 0
    def c():
        nonlocal count
        count += 1
        return count
    return c

x = counter()
print(x())
print(x())
print(x())

y = counter()
print(y())
print(x())
print(y())
print(y())