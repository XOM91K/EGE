l = [[int(d) for d in x.split()] for x in open('9.txt')]
ct = 0
for x in l:
    if len(set(x)) == 6:
        if (min(x) + max(x)) / 2 < (sum(x) - min(x) - max(x)) / 4:
            print(x)
            ct += 1
print(ct)