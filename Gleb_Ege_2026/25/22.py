def dels(d):
    l = []
    for x in range(1, int(d ** 0.5) + 1):
        if d % x == 0:
            l.append(x)
            l.append(d // x)
    return sorted(set(l))
for x in range(10000, 31623):
    x = x ** 2
    d = dels(x)
    if len(d) == 39:
        print(x, max([y for y in d if y % 2 != 0]))

100962304 24649
108826624 26569
114233344 27889
122589184 29929
131239936 32041
939790336 229441
971444224 237169
976562500 244140625
982634409 982634409
987467776 241081