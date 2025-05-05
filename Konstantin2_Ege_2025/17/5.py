l = [int(x) for x in open('5.txt')]
s  = max([v for v in l if str(v)[-2:] == '17'])
m = []
for i in range(len(l) - 2):
    p = [c for c in [l[i],l[i+1],l[i+2]] if len(str(c)) == 4]
    d  = [b for b in [l[i],l[i+1],l[i+2]] if str(b)[-1] in '05']
    if (l[i] + l[i + 1] + l[i + 2]) > s:
        if len(p) == 2:
            if len(d) >= 1:
                m.append(l[i] + l[i + 1] + l[i + 2])
print(len(m),max(m))