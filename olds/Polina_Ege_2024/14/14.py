d = 19 ** 81 + 23 ** 709 - 4
s = ''
while d > 0:
    s += str(d % 9)
    d //= 9
s = s[::-1]
for x in '1234567':
    s = s.replace(x, '#')
print(s.count('8#'))