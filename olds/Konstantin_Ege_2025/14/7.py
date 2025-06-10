d = 53 ** 123 + 65 ** 2222 - 172 ** 12
s = ''
while d > 0:
    s += str(d % 7)
    d //= 7
s = s[::-1]
n=0
for i in '12345':
    n += s.count('6' + i)
print(n)