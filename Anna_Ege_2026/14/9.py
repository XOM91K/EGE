def v9(n):
    s = ''
    while n > 0:
        s += str(n % 9)
        n //= 9
    return s[::-1]
for x in range(1, 10000):
    d = 9 ** 1942 + 9 * 6 ** 971 + 214 - x
    d = v9(d)
    if abs(d.count('2') - d.count('8')) == 471:
        print(x)