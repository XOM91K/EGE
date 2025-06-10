l = [int(x) for x in open('27.txt')]
ct = 0
s = []
rq = len([x for x in l if abs(x) % 10 == 7])
for x in range(len(l) - 1):
    if (str(l[x])[0] == '-' and str(l[x + 1])[0] != '-') or (str(l[x])[0] != '-' and str(l[x + 1])[0] == '-'):
        if l[x] + l[x + 1] < rq:
            ct += 1
            s.append(l[x] + l[x + 1])
print(ct, max(s))