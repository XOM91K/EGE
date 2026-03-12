def dels(d):
    dls = []
    for x in range(1, int(d ** 0.5) + 1):
        if d % x == 0:
            dls.append(x)
            dls.append(d // x)
    return sorted(set(dls))
for x in range(10000, 31623):
    x = x ** 2
    if x % 2 == 0:
        dls = dels(x)
        if len(dls) == 39:
            print(x, max([d for d in dls if d % 2 != 0]))
# 100962304 24649
# 108826624 26569
# 114233344 27889
# 122589184 29929
# 131239936 32041
# 893292544 218089
# 939790336 229441
# 971444224 237169
# 976562500 244140625
# 987467776 241081