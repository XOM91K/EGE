l = [[int(d) for d in x.split()] for x in open('736.txt')]
l = sorted(l, key=lambda d: d[1])
confs = [l[0]]
for x in l:
    if confs[-1][-1] + 20 <= x[0]:
        confs.append(x)
print(len(confs))
for x in confs:
    print(x)
print('-----')
for x in l:
    if x[0] > 1264:
        print(x)
print(1288-1236)