l = [sorted([int(d) for d in x.split()]) for x in open('10.txt')]
ct = 0

for x in l:#[35, 12, 10, 9, 11, 11, 11]
    if (len(set(x)) == 5 and (x.count(x[2]) == 3 or x.count(x[3]) == 3 or x.count(x[4]) == 3)):
        povt = (sum(x) - sum(set(x))) // 2
        if (sum(x) - povt * 3) / 4 < povt:
            ct +=1
            print(x, (sum(x) - sum(set(x))) // 2)
print(ct)