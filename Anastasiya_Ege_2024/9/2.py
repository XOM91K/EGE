l = [[int(d) for d in x.split()] for x in open('2.txt')]
summ = 0
k = 0
for x in l:
    k += 1
    povt = []
    for y in x:
        if x.count(y) > 1:
            povt.append(y)
    if len(povt) > 0:
        print(x)
        if (sum(povt) / len(povt)) < (sum(x) / len(x)):
            summ += k
print(summ)