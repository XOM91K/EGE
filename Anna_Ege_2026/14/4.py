def v15(n):
    s = []
    while n > 0:
        s.append(str(n % 15))
        n //= 15
    return s[::-1]

d = 11 * 15 ** 65 + 18 * 15 ** 38 - 14 * 15 ** 17 + 19 * 15 ** 11 + 18338
d = v15(d)
print(d)
print(set(d))
print(len(set(d)))