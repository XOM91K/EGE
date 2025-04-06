def v25(n):
    s = []
    while n > 0:
        s.append(str(n % 25))
        n //= 25
    return s[::-1]
a = 15625 ** 16 - 3125 ** 3 * 25 ** 19 + 625 ** 4 - 2005
a = v25(a)
print(a.count('0'))
print(a)