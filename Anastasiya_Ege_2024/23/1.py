def f(x, y):
    #задача №7118 на полякове
    # x - с какого числа мы идём
    # y - в какое число мы идём
    if x == y:
        return 1
    if x < y or x == 24:
        return 0
    if x > y:
        return f(x - 2, y) + f(x - 4, y)
print(f(34, 28) * f(28, 12))
