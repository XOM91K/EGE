def v37(n):
    s = []
    while n > 0:
        if n % 31 <= 17:
            s.append(n % 31)
        n //= 31
    return s[::-1]
d = 3 * 289 ** 2024 + 81 * 49 ** 121 - 9 * 16 ** 81 - 6011
d = v37(d)
print(sum(d))