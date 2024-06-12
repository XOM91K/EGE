d = 7 * 5 ** 1984 - 6 * 25 ** 777 + 5 * 125 ** 333 - 4
l = []
while d > 0:
    l.append(d % 5)
    d //= 5
l = l[::-1]
print(sum(l))
