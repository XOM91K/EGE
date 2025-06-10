d = 11 * 15 ** 65 + 18 * 15 ** 38 - 14 * 15 ** 17 + 19 * 15 ** 11 + 18338
s = []
while d > 0:
    s.append(d % 15)
    d //= 15
s = s[::-1]
print(s)
print(set(s))