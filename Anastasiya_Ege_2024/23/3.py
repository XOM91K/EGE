def f(x, y):
    #6778 на полякове
    if x == y:
        return 1
    if x > y or x == 17:
        return 0
    if x < y:
        return f(x + 2, y) + f(x + 3, y) + f(x * 2, y)
print(f(3, 10) * f(10, 25))