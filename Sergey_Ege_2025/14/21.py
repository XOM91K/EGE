def v5(n):
    s = ''
    while n > 0:
        s += str(n % 5)
        n //= 5
    return s[::-1]
for x in range(1, 5555):
    d = 5 ** 150 + 5 ** 135 - x
    d = v5(d)
    if d.count('4') == 134:
        print(x)