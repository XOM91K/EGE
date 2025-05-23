def v5(n):
    s = ''
    while n > 0:
        s += (str(n % 5))
        n //= 5
    return s[::-1]
for x in range(2, 2026):
    d = 5 ** 2025 + 5 ** 200 - x
    d = v5(d)
    if d.count('4') > 198:
        print(x, d.count('4'))