def v7(n):
    s = ''
    while n > 0:
        s += str(n % 7)
        n //= 7
    return s[::-1]
d = 4 * 7 ** 24 + 6 * 7 ** 13 + 5 * 49 ** 4 + 2 * 343 ** 2 + 10
for x in range(2_900_000_0, 10 ** 15):
    g = d - x
    g = v7(g)
    print(g.count('6'), g.count('0'), x, g)
    if g.count('6') > g.count('0'): #11 12 #4000000000060000456261122
        print(x)
        break