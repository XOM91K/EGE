def v12(n):
    s = []
    while n > 0:
        s.append(n % 12)
        n //= 12
    return s[::-1]
d = 12 ** 34 + 7 * 12 ** 26 - 3 * 12 ** 16 + 2 * 12 ** 5 + 552
print(len(set(v12(d))))