d = 3 * 11 ** 58 + 15 * 11 ** 55 - 99 * 11 ** 18 + 125 * 11 ** 9 + 381
l = []
while d > 0:
    l.append(d % 11)
    d //= 11
print(len(set(l)))