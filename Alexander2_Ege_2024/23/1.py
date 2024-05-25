def f(x, y, count):
    if x > y or (x == y and count != 1):
        return 0
    if x == y:
        return 1
    if x < y:
        return f(x + 1, y, count) + f(x + 2, y, count) + f(x * 2, y, count + 1)
print(f(2, 12, 0))