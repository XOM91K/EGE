l = [[int(d) for d in x.split()] for x in open('4.txt')]
ct = 0
for x in l:
    if len(set(x)) == len(x) - 1:
        povt = sum(x) - sum(set(x))
        if (sum(x) - povt * 2) / 4 <= povt * 2:
            ct += 1
print(ct)