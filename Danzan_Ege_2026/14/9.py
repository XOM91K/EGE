def v27(d):
    s = []
    while d > 0:
        s.append(d%27)
        d//=27
    return s[::-1]
d = 5 * 729 ** 2024 + 3 * 243 ** 1413 - 7 * 81 ** 169 - 2 * 9 ** 107 + 3017
d = v27(d)
sm = 0
for x in d:
    if x <= 25 and x % 2 == 0:
        sm += x
print(sm)