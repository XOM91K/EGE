d = 53 ** 123 + 65 ** 2222 - 172 ** 12
s = ''
while d > 0:
    s += str(d % 7)
    d //= 7
s = s[::-1]
ct = 0
for x in range(1, 6):
    ct += s.count('6' + str(x))
print(ct)