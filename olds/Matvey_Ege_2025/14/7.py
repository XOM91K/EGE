d = 53 ** 123 + 65 ** 2222 - 172 ** 12
s = ''
while d > 0:
    s += str(d % 7)
    d //= 7
s = s[::-1]

print(s.count('61') + s.count('62') + s.count('63') + s.count('64') + s.count('65'))