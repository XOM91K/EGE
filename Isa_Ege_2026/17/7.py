l = [int(x) for x in open('7.txt')]
mx2 = max([x for x in l if len(str(abs(x))) == 2])
mx = []
A = []
for x in range(len(l) - 3):
    if str(l[x])[-1] == str(l[x + 1])[-1] == str(l[x + 2])[-1] == str(l[x + 3])[-1]:
        A.append(l[x] + l[x + 1] + l[x + 2] + l[x + 3])
A = max(A)
for x in range(len(l) - 4):
    pt = sorted([l[x], l[x + 1], l[x + 2], l[x + 3], l[x + 4]])
    if pt[0] < A and pt[1] >= A:
        if sum(pt) % mx2 == 0:
            mx.append(sum(pt))
print(len(mx), min(mx))