l = [[int(d) for d in x.split()] for x in open('9.txt')]
ct = 0
for x in l:
    if len(set(x)) == 6:
        if (max(x) + min(x)) / 2 < (sum(x) - max(x) - min(x)) / 4:
            ct += 1
print(ct)