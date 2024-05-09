l = [[int(d) for d in x.split()] for x in open('6.txt')]
l = sorted(l, key=lambda d: d[1]) #сортировка по 2-му элементу в двумерном списке
confs = [l[0]]
for x in l:
    if x[0] >= confs[-1][1]:
        confs.append(x)
print(confs)
for x in l:
    if x[0] > 991 and x[1] > 1028:
        print(x)
print(len(confs), confs)