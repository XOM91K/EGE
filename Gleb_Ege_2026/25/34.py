def f(n):
    l = []
    x = 2
    while x * x <= n:
        while n % x == 0:
            l.append(x)
            n //= x
        x += 1
    if n > 1:
        l.append(n)
    return l
ct = 0
for x in range(2_626_695_892, 5_000_000_000):
    a = f(x)
    if len(a) == 2:
        if str(a[0]).count('67') == 1 and str(a[1]).count('67') == 1:
            print(x, min(a))
            ct += 1
            if ct == 5:
                break