l = [[int(d) for d in x.split()] for x in open('14.txt')]
k = 0
for x in l:
    k += 1
    povt3 = [d for d in x if x.count(d) == 3]
    povt1 = [d for d in x if x.count(d) == 1]
    if len(set(povt3)) == 2 and len(povt1) == 1:
        if (sum(povt3) / len(povt3)) < sum(povt1):
            print(k, x)