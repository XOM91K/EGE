def v27(d):
    s = []
    while d > 0:
        s.append(d % 27)
        d //= 27
    return s[::-1]
d = 2 * 2187 ** 567 + 729 ** 566 - 2 * 243 ** 565 + 81 ** 564 - 2 * 27 ** 563 - 6561
d = v27(d)
ct = 0
for x in d:
    if x > 9 and x % 2 == 0:
        ct += 1
print(ct)