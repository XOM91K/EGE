d = 8 ** 1006 + 5 ** 1947 + 505
s = []
while d > 0:
    s.append(d % 7)
    d //= 7
print((s.count(6) * 6) - (s.count(2) * 2))