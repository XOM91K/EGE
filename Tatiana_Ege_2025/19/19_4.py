def f(s1, s2, m):
    if s1 + s2 >= 541:
        return m % 2
    if m == 0:
        return 0
    h = [f(s1 + 10, s2, m - 1), f(s1, s2 + 10, m - 1), f(s1 * 2, s2, m - 1), f(s1, s2 * 2, m - 1)]
    return any(h) if (m - 1) % 2 == 0 else all(h)
print([S for S in range(1, 501) if f(6, S, 3) and not f(6, S, 2)])
