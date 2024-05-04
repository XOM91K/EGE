l = [sorted([int(d) for d in x.split()]) for x in open('9.txt')]
ct = 0
for x in l:
    if len(set(x)) == 4 and (x.count(x[2]) == 3 or x.count(x[3]) == 3):
        povt = (sum(x) - sum(set(x))) // 2
        if (sum(x) - povt * 3) / 3 <= povt * 3:
            ct += 1
print(ct)
