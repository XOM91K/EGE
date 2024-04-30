l = sorted([int(x) for x in open('14.txt')])
sm = 99987
i = 0
ct = 0
while sm - l[i] >= 0:
    sm -= l[i]
    i += 1
    ct += 1
print(ct)
sm += l[i - 1]
for x in range(len(l) - 1, -1, -1):
    if sm - l[x] >= 0:
        print(l[x])
        break