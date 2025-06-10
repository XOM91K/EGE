def v27(d):
    s = []
    while d > 0:
        s.append(d % 27)
        d //= 27
    return s[::-1]
w = 5 * 729 ** 2024 + 3 * 243 ** 1413 - 7 * 81 ** 169 - 2 * 9 ** 107 + 3017
w = v27(w)
sm = 0
for x in range(2, 25, 2):
    sm += w.count(x) * x
print(sm)