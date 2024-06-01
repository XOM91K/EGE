#https://kompege.ru/variant?kim=25028282
l = [[int(d) for d in x.split()] for x in open('1.txt')]
for x in range(len(l)):
    l[x] = [l[x][0], l[x][1], x + 1]
l = sorted(l, key=lambda d: min(d[:-1]))
trn = [0] * len(l)
left = 0
right = -1
last = 0
for x in range(len(l)):
    if min(l[x][:-1]) == l[x][0]:
        trn[left] = l[x][2]
        left += 1
    elif min(l[x][:-1]) == l[x][1]:
        trn[right] = l[x][2]
        right -= 1
    last = l[x][2]
print(last, trn.index(last))