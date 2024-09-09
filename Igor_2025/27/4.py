l = [[float(d) for d in x.split()] for x in open('4.txt')]
clusters = [[],[]]
for x in l:
    if -2 <= x[0] <= 1:
        clusters[0].append(x)
    else:
        clusters[1].append(x)
sl = {}
for s in clusters[0]:
    if f'{s[0]}+{s[1]}' not in sl:
        sl[f'{s[0]}+{s[1]}'] = []
    for c in clusters[0]:
        sl[f'{s[0]}+{s[1]}'].append(((c[0] - s[0]) ** 2 + (c[1] - s[1]) ** 2) ** 0.5)
    sl[f'{s[0]}+{s[1]}'] = sum(sl[f'{s[0]}+{s[1]}'])
print(sl)
sl1 = {}
for s in clusters[1]:
    if f'{s[0]}+{s[1]}' not in sl1:
        sl1[f'{s[0]}+{s[1]}'] = []
    for c in clusters[1]:
        sl1[f'{s[0]}+{s[1]}'].append(((c[0] - s[0]) ** 2 + (c[1] - s[1]) ** 2) ** 0.5)
    sl1[f'{s[0]}+{s[1]}'] = sum(sl1[f'{s[0]}+{s[1]}'])
print(sl1)
mn1 = 10 ** 10
tch1 = ''
for x in sl:
    if sl[x] < mn1:
        mn1 = sl[x]
        tch1 = x
mn2 = 10 ** 10
tch2 = ''
for x in sl1:
    if sl1[x] < mn2:
        mn2 = sl1[x]
        tch2 = x
print(tch1, mn1)
print(tch2, mn2)
tch1 = [float(d) for d in tch1.split('+')]
tch2 = [float(d) for d in tch2.split('+')]
Px = (tch1[0] + tch2[0]) / 2 * 10000
Py = (tch1[1] + tch2[1]) / 2 * 10000
print(int(Px), int(Py))