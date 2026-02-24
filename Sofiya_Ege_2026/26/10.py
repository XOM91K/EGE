l = [[int(d) for d in x.split()] for x in open('10.txt')]
l2 = []
for x in range(len(l)):
    l2.append([l[x][0], x + 1, 'ш'])
    l2.append([l[x][1], x + 1, 'о'])
l2 = sorted(l2, key=lambda d: d[0])
tr = [-1] * 997
print(tr)
st = 0
fn = -1
print(l2)
nomera = []
for x in range(len(l2)):
    if l2[x][-1] == 'ш' and l2[x][1] not in nomera:
        tr[st] = l2[x][1]
        nomera.append(l2[x][1])
        print(l2[x][1])
        st += 1
    elif l2[x][1] not in nomera:
        tr[fn] = l2[x][1]
        nomera.append(l2[x][1])
        print(l2[x][1])
        fn -= 1
print(tr)
print(tr.index(895))
# 0, 1, 2, 3, 4 , 5