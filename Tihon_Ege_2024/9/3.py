l = [[int(d) for d in x.split()] for x in open('3.txt')]
ct = 0
for x in l:
    if len(set(x)) == 5:
        povt = sum(x) - sum(set(x))
        sr = (sum(x) - povt * 2) / 4
        if sr <= povt * 2:
            ct += 1
print(ct)