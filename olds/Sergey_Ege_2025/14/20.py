def v5(n):
    s = ''
    while n > 0:
        s += str(n % 5)
        n //= 5
    return s[::-1]
d = 7 * 5 ** 1984 - 6 * 25 ** 777 + 5 * 125 ** 333 - 4
print(sum(map(int, v5(d))))