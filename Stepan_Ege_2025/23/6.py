l = []
def f(x, c):
    if c > 5:
        return 0
    if c <= 5:
        l.append(x)
    return f(x + 1, c + 1) + f(x * 2, c + 1)
print(f(1, 0))
print(sorted(l))