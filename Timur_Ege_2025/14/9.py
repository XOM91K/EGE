def v9(n):
    s = ''
    while n > 0:
        s += str(n % 9)
        n //= 9
    return s[::-1]
for x in range(1, 10000):
    d = 81 ** 20 - 9 ** x + 50
    d = v9(d)
    if sum(map(int, str(d))) == 138:
        print(x)