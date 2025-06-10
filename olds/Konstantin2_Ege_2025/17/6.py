l = [int(x) for x in open('6.txt')]
a = max([v for v in l if str(v)[-1] == '7'])
s = []
ct = 0
for i in range(len(l) - 2):
    p = [v for v in [l[i],l[i+1],l[i+2]] if v %2 != 0]
    c = [v for v in [l[i],l[i+1],l[i+2]] if v > a]
    if len(p) == 2 and len(c) == 1:
        s.append(l[i])
        s.append(l[i + 1])
        s.append(l[i + 2])
        ct += 1
print(ct,sum(set(s)) / len(set(s)))