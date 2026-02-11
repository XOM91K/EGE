def f(s1, s2, m):
    if s1 + s2 >= 323: return m % 2 == 0
    if m == 0: return m == 0
    h = [f(s1 + 3, s2, m - 1), f(s1, s2 + 3, m - 1), f(s1 * 2, s2, m - 1), f(s1, s2 * 2, m - 1)]
    return any(h) if (m - 1) % 2 == 0 else all(h)


print([s2 for s2 in range(1, 200) if f(123, s2, 2)])
print([s2 for s2 in range(1, 200) if (not f(123, s2, 1))and f(123, s2, 3)])
print([s2 for s2 in range(1, 200) if not f(123, s2, 2) and f(123, s2, 4)])
