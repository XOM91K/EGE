l = [[int(d) for d in x.split()]for x in open("9.txt")]
ct = 0
for x in l:
    x = sorted(x)
    if x.count(x[-1]) == 1:
        if len(set(x)) < 6:
            if x[-1] / ((sum(x) - x[-1])/5) > 3:
                ct += 1
print(ct)