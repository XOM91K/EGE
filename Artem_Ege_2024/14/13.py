d = 625 ** 90 + 125 ** 120 - 5 * 25
s = []
while d > 0:
    s.append(d % 25)
    d //= 25
print(s)