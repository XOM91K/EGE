l = [[int(d) for d in x.split()] for x in open('1546.txt')]
k = 0
for x in l:
    k += 1
    if sorted(x) == x:
        ch = [d for d in x if x.count(d) == 4]
        dv = [d for d in x if x.count(d) == 2]
        od = [d for d in x if x.count(d) == 1]
        if len(ch) == 4 and len(dv) == 2 and len(od) == 1:
            if max(ch + dv) <= od[0]:
                if k % 7 == 0:
                    print(k)