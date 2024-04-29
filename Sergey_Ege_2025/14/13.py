d = 4 * 8 ** 3032 + 3 * 16 ** 1956 + 870
s = []
while d > 0:
    s.append(d % 7)
    d //= 7
s = s[::-1]
s1 = s.count(3)
s2 = s.count(1)
print((s1 * 3) - s2)
