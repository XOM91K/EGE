d = 7 ** 103 - 6 * 7 ** 70 + 3 * 7 ** 57 - 98
s = ''
while d > 0:
    s += str(d % 7)
    d //= 7
s = s[::-1]
print(s)
print(s.count('6'))