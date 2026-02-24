l = [[int(d) for d in x.split()] for x in open('17.txt')]
l = sorted(l, key=lambda d: d[1])
confs = []
conf_hall = 0
for x in l:
    if x[0] - conf_hall >= 20:
        conf_hall = x[1]
        confs.append(x)
print(confs)
print(len(confs))
for x in l:
    if x[0] > 1264:
        print(x)