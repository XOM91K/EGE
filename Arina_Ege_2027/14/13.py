def v9(d):
    s = ''
    while d > 0:
        s += str(d % 9)
        d //= 9
    return s[::-1]
for x in range(1, 10000):
    if sum(map(int, str(v9((81 ** 20 - 9 ** x + 50))))) == 138:
        print(x)
        break