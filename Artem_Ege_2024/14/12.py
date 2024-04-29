s = 625 ** 90 + 125 ** 120 - 5 * 25
l = []
while s > 0:
    l.append(s % 25)
    s //= 25
print(sum(l) - 1)
