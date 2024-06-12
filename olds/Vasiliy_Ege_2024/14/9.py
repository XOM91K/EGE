d = 5 ** 55 + 5 ** 555 * 555 - 5
s = ''
while d > 0:
    s += str(d % 5)
    d //= 5
print(s[::-1].count('0'))