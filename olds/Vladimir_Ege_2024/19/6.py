import math
# -1, / 2, в первой куче 10 камней, S > 22
def g(s1, s2, p):
    if s1 + s2 <= 32 and (p == 4 or p == 2):
        return 1
    elif s1 + s2 > 32 and p == 4:
        return 0
    elif s1 + s2 <= 32 and p < 4:
        return 0
    if p % 2 == 0:
        return g(s1 - 1, s2, p + 1) and g(math.ceil(s1 / 2), s2, p + 1) and g(s1, s2 - 1, p + 1) and g(s1, math.ceil(s2 / 2), p + 1)
    else:
        return g(s1 - 1, s2, p + 1) or g(math.ceil(s1 / 2), s2, p + 1) or g(s1, s2 - 1, p + 1) or g(s1, math.ceil(s2 / 2), p + 1)
for x in range(23, 100):
    if g(10, x, 0):
        print(x)