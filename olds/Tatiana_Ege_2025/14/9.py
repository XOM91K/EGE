def convert(a):
    s = []
    while a > 0:
        s.append(str(a % 25))
        a = a // 25
    return s[::-1]
f = 3 * 3125 ** 8 + 2 * 625 ** 7 - 4 * 625 ** 6 + 3 * 125 ** 5 - 5 * 25 ** 4 - 2025
f = convert(f)
print(f)
print(f.count("0"))