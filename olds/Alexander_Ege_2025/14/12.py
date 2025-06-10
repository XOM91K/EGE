def v15(d):
    s = []
    while d > 0:
        s.append(d % 15)
        d //= 15
    return s[::-1]

n = 3 * 15 ** 1140 + 2 * 15 ** 1025 + 15 ** 923 - 3 * 15 ** 85 + 2 * 15 ** 74 + 3
n = v15(n)
mx = []
ct = 0
print(n)
for x in range(len(n) - 1):
    if n[x] == n[x + 1]:
        ct += 1
    else:
        mx.append(ct)
        ct = 0
print(mx)