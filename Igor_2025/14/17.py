def v27(d):
    res = []
    while d > 0:
        res.append(d % 27)
        d //= 27
    return res[::-1]
d = 7 * 729 ** 2048 + 3 * 243 ** 1413 - 7 * 81 ** 169 - 3 * 9 ** 107 + 2017
d = v27(d)
cnt = 0
for i in d:
    if i > 17:
        cnt += i
print(cnt)
