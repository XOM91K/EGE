def f(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    else:
        return f(x + 1, y) + f(x * 2, y) + f(x * 3, y)
ct = 0
for x in range(1, 200):
    if x % 2 == 0:
        ct += f(x, 15)
print(ct)