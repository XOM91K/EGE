l = [int(x) for x in open("5.txt")]
ct = []
print(l)
mx = max([d for d in l if d % 100 == 19])
for x in range(len(l) - 2):
    chety = []
    if len(str(abs(l[x]))) == 4:
        chety.append(l[x])
    if len(str(abs(l[x + 1]))) == 4:
        chety.append(l[x + 1])
    if len(str(abs(l[x + 2]))) == 4:
        chety.append(l[x + 2])
    if len(chety) == 2:
        if l[x] % 3 == 0 or l[x + 1] % 3 == 0 or l[x + 2] % 3 == 0:
            if l[x] + l[x + 1] + l[x + 2] > mx:
                ct.append(l[x] + l[x + 1] + l[x + 2])
print(len(ct), max(ct))
