l = [[int(d) for d in x.split()] for x in open('9.txt')]
r = [[x, 0] for x in range(1, 1441)]
print(l)
for x in range(len(r)):
    for y in l:
        if y[0] <= r[x][0] <= y[1]:
            r[x][1] += 1
print(r)
pikov = 0
ct = 0
for x in range(len(r) - 1):
    if r[x][1] == r[x + 1][1] == 644:
        ct += 1
    else:
        if ct == 1:

print(max(r, key=lambda d: d[1])[-1])