l = [[int(d) for d in x.split()] for x in open('7.txt')]
ct = 0
for x in l:
    if len(set(x)) == 4:
        povt = sum(x) - sum(set(x))
        if povt * 2 > sum(x) - (povt * 2):
            ct += 1
print(ct)