def dels(d):
    l = []
    for x in range(1, int(d ** 0.5) + 1):
        if d % x == 0:
            l.append(x)
            l.append(d // x)
    return sorted(set(l))
for x in range(10_000, 31623):
    dl = dels(x ** 2)
    l = dl
    if len(l) == 39 and x ** 2 % 2 == 0:
        print(x ** 2, [d for d in l if d % 2 != 0][-1])
print(100_000_000 ** 0.5)
print(1000_000_000 ** 0.5)
100962304 24649
108826624 26569
114233344 27889
122589184 29929
131239936 32041
893292544 218089
939790336 229441
971444224 237169
976562500 244140625
987467776 241081