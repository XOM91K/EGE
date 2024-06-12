#https://kompege.ru/variant?kim=25028275
l = [[int(d) for d in x.split()] for x in open('5.txt')]
l = sorted(l, key=lambda d: d[1])
confs = [l[0]]
for x in l:
    if x[0] >= confs[-1][1]:
        confs.append(x)
for x in l:
    if x[0] >= 991 and x[1] > 1028:
        print(x)
print(len(confs))
print(confs)