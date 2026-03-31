def f(x, y, ct):
    if x > y or x == 17 or x == 28:
        return 0
    if x == 14 or x == 18:
        ct += 1
    if x == y and ct > 0:
        return 1
    if x == y and ct <= 0:
        return 0
    if x < y:
        return f(x + 2, y, ct) + f(x + 3, y, ct) + f(x * 2, y, ct)
# print(f(8, 48) - (f(8, 14) * f(14, 18) * f(18, 48)))
# print((f(8, 14) * f(14, 48)) + (f(8, 18) * f(18, 48)) - (f(8, 14) * f(14, 18) * f(18, 48)))
print(f(8, 48, 0))