l = [[int(d) for d in x.split()] for x in open('7.txt')]
l = sorted(l, key=lambda d: d[1])
conference_zall = 0
mer = []
ct = 0
for x in l:
    if x[0] >= conference_zall:
        conference_zall = x[1] + 20
        mer.append(x)
        ct += 1
mx = []
for x in l:
    print(x)
    if x[0] > mer[-1][0]:
        mx.append(x[0])
print(ct)
print(max(mx) - mer[-2][1])