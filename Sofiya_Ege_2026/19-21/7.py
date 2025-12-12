def f(s1, s2, m):
    if s1+s2>=212: return m%2==0
    if m==0: return 0
    h=f(s1+s2, s2, m-1), f(s1, s1+s2, m-1)
    return any(h) if (m-1)%2==0 else all(h)
print('19', max([s2 for s2 in range(0, 112) if not f(100, s2, 1)]))
print('20', [s2 for s2 in range(0, 112) if not f(50, s2, 1) and f(50, s2, 3)])
print('21', max([s2 for s2 in range(0, 10000) if not f(10, s2, 2) and f(10, s2, 4)]))