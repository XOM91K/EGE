l = [[int(d) for d in x.split()] for x in open("698.txt")]
ct = 0
for x in l:
    if len(set(x)) == 6 and (max(x) + min(x)) / 2 > (sum(x) - min(x) - max(x)) / 4:
        ct += 1
print(ct)