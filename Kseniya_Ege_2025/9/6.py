l = [sorted([int(d) for d in x.split()]) for x in open('6.txt')]
ct = 0
for x in l:
    if len(set(x)) == 3:
        if (x[-1] + x[-2]) > (x[0]+ x[1]) * 2:
            if max(x) % min(x) != 0:
                ct+=1
print(ct)