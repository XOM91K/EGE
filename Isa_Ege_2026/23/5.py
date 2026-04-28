def f(x, y, k):
    if x == 40 or x == 20 or x == 30:
        k += 1
    if x < y:
        return 0
    if x == y and k >= 2:
        return 1
    if x == y and k < 2:
        return 0
    if x > y:
        return f(x - 1, y, k) + f(x - 3, y, k) + f(x // 3, y, k)
print(f(49, 12, 0))