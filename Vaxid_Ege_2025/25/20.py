def f(n):
    dels = []
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            dels.append(x)
            dels.append(n // x)
    return sorted(set(dels))


cnt = 0
for i in range(106, 10**9, 106):
    m = len(f(i))
    l = max(f(i))
    if m == 7:
        print(i, l)