l = [int(x) for x in open('3.txt')]
mx = max([x for x in l if str(x)[-1] == '7'])
sr = []
ct = 0
for x in range(len(l) - 2):
    if ((l[x] % 2) != 0) + ((l[x + 1]) % 2 != 0) + ((l[x + 2]) % 2 != 0) == 2:
        if ((l[x] > mx) + (l[x + 1] > mx) + (l[x + 2] > mx)) == 1:
            sr.append(l[x])
            sr.append(l[x + 1])
            sr.append(l[x + 2])
            ct += 1
sr = set(sr)
sr = sum(sr) / len(sr)
print(ct, sr)