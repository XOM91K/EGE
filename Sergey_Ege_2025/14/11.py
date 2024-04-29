d = 3 ** 72 + 6 * 3 ** 50 - 7 * 3 ** 26 + 2 * 3 ** 15 + 155
l = []
while d > 0:
    l.append(d % 9)
    d //= 9
print(l)
print(len(set(l)))