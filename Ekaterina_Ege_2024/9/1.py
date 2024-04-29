l = [[int(d) for d in x.split()] for x in open('1.txt')]
ct = 0
for x in l:
    if len(set(x)) == 5:
        povt = sum(x) - sum(set(x))
        if (sum(x) - povt * 2) / 4 <= povt * 2:
            ct += 1
print(ct)