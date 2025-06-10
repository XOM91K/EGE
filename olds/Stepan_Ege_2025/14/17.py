d = 3 * 289 ** 2024 + 81 * 49 ** 121 - 9 * 16 ** 81 - 6011
s = []
while d > 0:
    s.append(d % 31)
    d //= 31
s = s[::-1]
men = [y for y in s if y <= 17]
print(sum(men))