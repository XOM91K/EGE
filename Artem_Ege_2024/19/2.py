#+1, *2 >=259 [17, S] 1 <= S <= 241
def g(s1, s2, p):
    if s1 + s2 >= 259 and (p == 4 or p == 2):
        return 1
    elif s1 + s2 < 259 and p == 4:
        return 0
    elif s1 + s2 >= 259 and p < 4:
        return 0
    if p % 2 == 0:
        return g(s1 + 1, s2, p + 1) and g(s1 * 2, s2, p + 1) and g(s1, s2 + 1, p + 1) and g(s1, s2 * 2, p + 1)
    else:
        return g(s1 + 1, s2, p + 1) or g(s1 * 2, s2, p + 1) or g(s1, s2 + 1, p + 1) or g(s1, s2 * 2, p + 1)
for S in range(1, 242):
    if g(17, S, 0) == 1:
        print(S)

#61
#112 120
#111