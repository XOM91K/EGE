d = 3 * 15 ** 1140 + 2 * 15 ** 1025 + 15 ** 923 - 3 * 15 ** 85 + 2 * 15 ** 74 + 3
def v15(n):
    s = []
    while n > 0:
        s.append(n % 15)
        n //= 15
    return s[::-1]
d = v15(d)
print(d)