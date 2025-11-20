def f(s, m):
    if s <= 17: return m % 2 == 0
    if m == 0: return 0
    h = [f(s - 1, m - 1), f(s // 3 if s % 3 == 0 else s - 2, m - 1), f(s // 5 if s % 5 == 0 else s - 3, m - 1)]
    return any(h) if (m - 1) % 2 == 0 else all(h)


print('19', min([s for s in range(18, 100) if f(s, 2)]))
print('20', [s for s in range(18, 100) if not f(s, 1) and f(s, 3)])
print('21', [s for s in range(18, 100) if not f(s, 2) and f(s, 4)])
