def v15(n):
    ost = []
    while n > 0:
        ost += str(n % 15)
        n //= 15
    return ost[::-1]
d = 11 * 15 ** 65 + 18 * 15 ** 38 - 14 * 15 ** 17 + 19 * 15 ** 11 + 18338
print(len(set(v15(d))))