def f(x, y, ct):
    if x == 14 or x == 18:
        ct += 1
    if x > y:
        return 0
    if x == y and ct > 0:
        return 1
    if x == y and ct == 0:
        return 0
    if x < y:
        return f(x + 1, y, ct) + f(x * 2, y, ct) + f(x * 3, y, ct)
print(f(6, 48, 0))
# print(f(6, 14) * f(14, 18) * f(18, 48))
# print(f(6, 14) * f(14, 48))
# print(f(6, 18) * f(18, 48))
# print(45+48-24)