d = 12 ** 34 + 7 * 12 ** 26 - 3 * 12 ** 16 + 2 * 12 ** 5 + 552
s = []
while d > 0:
    s.append(d % 12)
    d //= 12
print(len(set(s[::-1])))