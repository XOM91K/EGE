def v15(d):
    s = []
    while d > 0:
        s.append(d % 15)
        d //= 15
    return s[::-1]
g = 3 * 15 ** 1140 + 2 * 15 ** 1025 + 15 ** 923 - 3 * 15 ** 85 + 2 * 15 ** 74 + 3
g = v15(g)
ln = 1
mx_ln = 1
for x in range(len(g) - 1):
    if g[x] == g[x + 1]:
        ln += 1
    else:
        mx_ln = max(mx_ln, ln)
        ln = 1
print(mx_ln)