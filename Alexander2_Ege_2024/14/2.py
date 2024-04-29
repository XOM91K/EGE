def v7(d):
    s = ''
    while d > 0:
        s += str(d % 7)
        d //= 7
    return s[::-1]
d = 6 * 343 ** 1156 - 5 * 49 ** 1147 + 4 * 7 ** 1153 - 875
d = v7(d)
print(sum(map(int, d)))