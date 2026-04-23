def f(x, y, ct):
    if x < y:
        return 0
    if x == 40 or x == 30 or x == 20:
        ct += 1
    if x == y and ct >= 2:
        return 1
    if x == y and ct < 2:
        return 0
    if x > y:
        return f(x - 1, y, ct) + f(x - 3, y, ct) + f(x // 3, y, ct)
print(f(49, 12, 0))