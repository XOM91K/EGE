l = [[int(d) for d in x.split()] for x in open('9.txt')]
l = sorted(l, key=lambda d: d[1])
ct = 0
time = 0
conf = 0
confs = []
for x in l:
    if x[0] - 10 >= conf:
        conf = x[1]
        ct += 1
        confs.append([x[0], x[1]])
print(ct)
l = l[::-1]
for x in l:
    time = max(time, x[0] - confs[-2][1])
print(time)