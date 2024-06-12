def v3(n):
    s = ''
    while n > 0:
        s += str(n % 3)
        n //= 3
    return s[::-1]
for x in range(1, 2001):
    if v3(3 ** 100 - x).count('0') == 2:
        print(x)
        