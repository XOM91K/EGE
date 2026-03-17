def v3(n):
    d = []
    while n > 0:
        d.append(n % 3)
        n = n // 3
    return d[::-1]
for x in range(100000):
    n=3**200+3**10-x
    n = v3(n)
    if n.count(2)==200:
        print(x)