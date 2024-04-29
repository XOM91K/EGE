l = [[int(d) for d in x.split()] for x in open('19.txt')]
l = sorted(l, key=lambda x: x[1])
time_free = 0
ct_conf = 0
confs = []
for x in l:
    if x[0] - 20 >= time_free:
        time_free = x[1]
        ct_conf += 1
        confs.append([x[0], x[1]])

for x in range(len(l) - 1, -1, -1):
    if l[x][0] - 20 >= confs[-2][1]:
        print(abs(l[x][0] - confs[-2][1]))
        break
print(ct_conf)
print(confs)