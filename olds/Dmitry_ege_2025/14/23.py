def v31(d):
    s = []
    while d > 0:
        if d % 31 <= 17:
            s.append(d % 31)
        d //= 31
    return s[::-1]
x = 3 * 289 ** 2024 + 81 * 49 ** 121 - 9 * 16 ** 81 - 6011
x = v31(x)

print(sum(x))