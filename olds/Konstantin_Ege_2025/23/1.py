def g(x,y):
    if x == y:
        return 1
    if x < y or x == 20:
        return 0
    if x > y:
        return g(x - 6, y) + g(x - 1, y) + g(x // 4, y)
print(g(42, 12) * g( 12, 10) * g(10, 6))