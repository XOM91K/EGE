l = [[int(d) for d in x.split()] for x in open('6.txt')]
l = sorted(l, key=sum)
arena = 0
poedinki = []
for x in l:
    if x[0] >= arena:
        arena = x[0] + x[1]
        poedinki.append(x)
mx = 0
for x in l:
    if x[0] > poedinki[-1][0]:
        mx = max(mx, x[0])
print(poedinki)
print(len(poedinki), mx - sum(poedinki[-2]))