def v7(n):
    s = ''
    while n > 0:
        s += str(n % 7)
        n //= 7
    return s[::-1]
d = 53 ** 123 + 65 ** 2222 - 172 ** 12
d = v7(d)
print(d)
print(d.count('61') + d.count('62') + d.count('63') + d.count('64') + d.count('65'))