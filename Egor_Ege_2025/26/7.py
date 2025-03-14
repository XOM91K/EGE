l = [[int(d) for d in x.split()] for x in open('7.txt')]
l = sorted(l, key=lambda d: d[1])
print(l)
conference_zall = 0
ct = 0
for x in l:
    if x[0] >= conference_zall:
        conference_zall = x[1] + 20
        ct += 1
print(ct)