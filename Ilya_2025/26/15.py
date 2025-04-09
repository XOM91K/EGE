l = [[int(d) for d in x.split()] for x in open('15.txt')]
mest = 485
l = sorted(l, key=lambda d: (d[1] + d[2] + d[3], d[-1], d[0]))[::-1]
#print(l)
# for x in l:
#     print(x, x[1] + x[2] + x[3])
pol = sum(l[:mest][-1][1:4])
ct = 0
for x in l:
    if x[1] + x[2] + x[3] == pol:
        ct += 1

for x in range(len(l) - 1, -1, -1):
    if l[x][1] + l[x][2] + l[x][3] > pol:
        print(l[x][0])
        break
print(ct)
#print(l[:mest])