import itertools, math
m = []
for x in itertools.product('041', repeat=10):
    s = ''.join(x) + '<'
    while '4<' in s or '11<' in s or '00<' in s:
        if '11<' in s:
            s = s.replace('11<', '<9', 1)
        if '4<' in s:
            s = s.replace('4<', '<5', 1)
        if '00<' in s:
            s = s.replace('00<', '<92', 1)
    s = s.replace('<', '1')
    m.append(math.prod(map(int, s)))
print(max(m))
