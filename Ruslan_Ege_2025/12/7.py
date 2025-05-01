b = []
for n in range(4, 10000):
    s = 'D'+n*'G'
    while 'GGGG' in s or '333' in s or 'G3' in s:
        if 'GGGG' in s:
            s = s.replace('GGGG', '3', 1)
        if '333' in s:
            s = s.replace('333', 'G', 1)
        if 'G3' in s:
            s = s.replace('G3', '3G', 1)
    h = int(s, 20)
    if sum(map(int, str(h)))%5 == 0:
        b.append(n)
print(len(set(b)))