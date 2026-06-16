def f(s, m):
    if s<=20_007: return m%2==0
    if m==0: return 0
    h=[f(s-2, m-1), f(s-7, m-1), f(s//3, m-1)]
    return any(h) if (m-1)%2==0 else all(h)
# print([s for s in range(20_008,550_000) if not f(s, 1) and f(s,2)])
# print('20', [s for s in range(20_008,550_000) if f(s, 3) and not f(s, 1)])
print('21', [s for s in range(20_008,550_000) if not f(s, 2) and f(s, 4)])