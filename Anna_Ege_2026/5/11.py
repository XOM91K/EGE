def v3(n):
    s = ''
    while n > 0:
        s += str(n % 3)
        n //= 3
    return s[::-1]


for n in range(1, 1000):
    r = v3(n)
    if sum(map(int, v3(n))) % 2 == 0:
        r = '10' + r[2:] + '0'
    if n % 3 != 0:
        r += v3((n % 3) * 5)
    r = int(r, 3)
    if r >= 2026:
        print(n)
        break
