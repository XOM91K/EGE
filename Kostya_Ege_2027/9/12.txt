 l = [[int(d) for d in x.split()]for x in open("2.txt")]
ct = 0
for x in l:
    x = sorted(x)
    if len(set(x)) == 5:
        cht = [d for d in x if d % 2 == 0]
        n_cht = [d for d in x if d % 2 != 0]
        if len(n_cht) > len(cht):
            if sum(n_cht) < sum(cht):
                ct += 1
print(ct)