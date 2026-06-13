l = [[int(d) for d in x.split()] for x in open('1.txt')]
k = 0
for x in l:
    k += 1
    # 20 20 20 9 21 21 21
    povt3 = [d for d in x if x.count(d) == 3]
    povt1 = [d for d in x if x.count(d) == 1]
    if len(povt3) == 6:
        if sum(povt3) / 6 > povt1[0]:
            print(k, x)