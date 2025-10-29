def f(s, m):
    if s>=108: return m%2==0
    if m==0: return 0 # тернарный условный оператор
    h=[f(s+1, m-1), f(s * 2 if s % 2 != 0 else s * 1.5, m-1)]
    return any(h) if (m - 1) % 2 == 0 else all(h)
print('19', max([s for s in range(1, 108) if f(s, 2)]))
print('20', [s for s in range(1, 108) if not f(s, 1) and f(s, 3)])
print('21', [s for s in range(1, 108) if not f(s, 2) and f(s, 4)])