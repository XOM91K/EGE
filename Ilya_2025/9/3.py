l = [sorted([int(d) for d in x.split()]) for x in open('3.txt')]
ct = 0
for x in l:
    if len(set(x)) == 5:
        if (sum(x) - (sum(x) - sum(set(x))) * 2) / 4 <= (sum(x) - sum(set(x))) * 2:
            ct += 1
print(ct)