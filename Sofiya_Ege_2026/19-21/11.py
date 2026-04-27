import math
def f(s1, s2, m):
    if s1+s2<=60: return m%2==0
    if m==0: return 0
    h=[f(s1-5, s2, m-1), f(s1, s2-3, m-1), f(math.floor(s1//2), s2, m-1), f(s1, math.ceil(s2//2), m-1)]
    return any(h) if (m-1)%2==0 else all(h)
print([s2 for s2 in range(5, 151) if f(130, s2, 2)])
print([s2 for s2 in range(5, 151) if not f(130, s2, 1) and f(130, s2, 3)])
print(math.prod([s2 for s2 in range(5, 151) if not f(130, s2, 1) and not f(130, s2, 3) and f(130, s2, 3) and f(130, s2, 5)]))