def f(x, y):
    if x < y:
        return 0
    if x == y:
        return 1
    if x > y:
        return f(x - 4, y) + f(x - 7, y) + f(int(x ** 0.5), y)
print(f(44, 22) * f(22, 3))
# print(81 ** 2)
# print(81 ** 4)
# print(81 ** 0.5)
#print(int(82 ** 0.5))