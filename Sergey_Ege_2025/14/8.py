def pt(n):
    s = []
    while n > 0:
        s.append(n % 15)
        n //= 15
    return s[::-1]
d = 11 * 15 ** 65 + 18 * 15 ** 38 - 14 * 15 ** 17 + 19 * 15 ** 11 + 18338
print(len(set(pt(d))))
