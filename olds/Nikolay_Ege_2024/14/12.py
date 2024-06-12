d = 5 * 216 ** 1256 - 5 * 36 ** 1146 + 4 * 6 ** 1053 - 1087
s = []
while d > 0:
    s.append(d % 6)
    d //= 6
print(sum(s))