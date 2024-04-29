d = 12 * 7 ** 135 + 11 * 7 ** 92 + 63 * 7 ** 22 + 17 * 7 ** 11 + 157
def v7(n):
    s = ''
    while n > 0:
        s += str(n % 7)
        n //= 7
    return s[::-1]
print(set(v7(d)))