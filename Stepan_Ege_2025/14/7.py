d = 3 * 3125 ** 8 + 2 * 625 ** 7 - 4 * 625 ** 6 + 3 * 125 ** 5 - 5 * 25 ** 4 - 2025
s = []
while d > 0:
    s.append(d % 25)
    d //= 25
s = s[::-1]
print(s)
print(s.count(0))