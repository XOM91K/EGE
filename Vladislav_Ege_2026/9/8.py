l = [[int(d) for d in x.split()] for x in open('8.csv')]
k = 0
for x in l:
    k += 1
    if x == sorted(x):
        povt4 = [d for d in x if x.count(d) == 4]
        povt2 = [d for d in x if x.count(d) == 2]
        povt1 = [d for d in x if x.count(d) == 1]
        if len(povt4) == 4 and len(povt2) == 2 and len(povt1) == 1:
            if max(max(povt4), max(povt2)) <= povt1[0]:
                if k % 7 == 0:
                    print(k)