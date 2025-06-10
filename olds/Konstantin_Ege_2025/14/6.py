d = 7 ** 1003 + 6 * 7 ** 1104 - 3 * 7 ** 57 + 294
s = ''
while d > 0:
    s += str(d % 7)
    d //= 7
s = s[::-1]
print(sum(map(int, s)))