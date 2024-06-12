def v9(n):
    s = ''
    while n > 0:
        s += str(n % 9)
        n //= 9
    return s[::-1]
d = 7 * 729 ** 543 - 6 * 81 ** 765 - 5 * 9 ** 987 - 20
print(v9(d).count('8'))
