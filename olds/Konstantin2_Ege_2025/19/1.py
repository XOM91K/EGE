def f(k, k2, m):
    if k + k2 >= 79:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(k + 1, k2, m - 1), f(k * 2, k2, m - 1), f(k, k2 + 1, m - 1), f(k, k2 * 2, m - 1)]
    return any(h) if m % 2 != 0 else all(h)
print('№19', min([s for s in range(1, 79) if f(7, s, 2)]))
print('№20', ([s for s in range(1, 79) if f(7, s, 3)]))
print('№21', min([s for s in range(1, 79) if f(7, s, 4)]))