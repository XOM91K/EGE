def f(x):
    B = 23<=x<=37
    C = 41<=x<=73
    A = a1<=x<=a2
    return not(((not B) <= C) <= A)

ox = [y for x in (23, 37, 41, 73) for y in (x, x+0.01, x-0.01)]

m = []
for a1 in ox:
    for a2 in ox:
        if a2>a1 and all(f(x) == 0 for x in ox):
            m.append(a2-a1)
print(min(m))