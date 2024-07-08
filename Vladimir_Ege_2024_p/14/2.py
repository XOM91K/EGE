def v31(d):
    sm = 0
    while d > 0:
        if d % 31 <= 17:
            sm += d % 31
        d //= 31
    return sm
d = 3 * 289 ** 2024 + 81 * 49 ** 121 - 9 * 16 ** 81 - 6011
print(v31(d))