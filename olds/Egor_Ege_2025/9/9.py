l = [[int(d) for d in x.split()] for x in open('9.txt')]
stolbs = [[d[x] for d in l] for x in range(6)]
ct = 0
#stolbs[0] stolbs[1]
for x in l:
    interests = 0
    for y in range(len(x)):
        sr = x[:y]
        sr2 = x[y + 1:]
        if x[y] not in sr and x[y] not in sr2:
            if stolbs[y].count(x[y]) < 170:
                interests += 1
    if interests >= 4:
        ct += 1
#10422
#10469
print(ct)