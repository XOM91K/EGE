l = [int(x) for x in open('13.txt')]
ot = 0
e = []
for i in l:
    if i < 0:
        ot += i
for x in range(len(l) - 2):
    c = [l[x], l[x + 1], l[x + 2]]
    if max(c) * min(c) > ot:
        e.append(l[x] + l[x + 1] + l[x + 2])
print(len(e), abs(max(e)))