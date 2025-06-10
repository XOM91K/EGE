def f(s1, s2, m):
    if s1 + s2 >= 212:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(s1 + s2, s2, m-1), f(s1, s1 + s2, m-1)]
    return any(h) if (m-1) % 2 == 0 else all(h)
print('19:', [s for s in range(1, 112) if not(f(100, s, 1))])
print('20:', [s for s in range(1, 200) if f(50, s, 3) and not f(50, s, 1)])
print('21:', [s for s in range(1, 112) if f(10, s, 4)])