# x - изначальное число
# y - конечное число
def f(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    if x < y:
        return f(x + 1, y) + f(x * 2, y) + f(x * 3, y)
print(f(2, 15) * f(15, 30))
