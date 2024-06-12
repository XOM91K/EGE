def v3(n):
    s = ''
    while n > 0:
        s += str(n % 3)
        n = n // 3
    return s[::-1]
for x in range(1, 2031):
    d = 3 ** 100 - x
    if v3(d).count('0') == 5:
        print(x)