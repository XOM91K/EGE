import math
print(math.perm(14, 7) * 4)
#17297280 * 4
print(int('10234567', 15))
#855_000_001
print(int('4edcba98', 15))
# 172544722
# 853425143
# разность: 680880422
# 0-15
    #[4, 14, 13, 12, 11, 10, 9, 8]

def v15(d):
    s = []
    while d > 0:
        s.append(d % 15)
        d //= 15
    return s[::-1]
#print(v15(855_000_000))
# for x in range(855_000_000, 172544722, -1):
#     g = v15(x)
#     if len(set(g)) == 8:
#         print(g, len(g))
#         break