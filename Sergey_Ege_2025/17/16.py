l = [int(x) for x in open('16.txt')]
ct = 0
mn = 10 ** 10
sr = [x for x in l if str(x)[-2:] == '28']
sr = sum(sr) / len(sr)
for x in range(len(l) - 2):
    if len(str(abs(l[x]))) == 4 or len(str(abs(l[x + 1]))) == 4 or len(str(abs(l[x + 2]))) == 4:
        k = 0
        if str(abs(l[x]))[-2:] == '11':
            k += 1
        if str(abs(l[x + 1]))[-2:] == '11':
            k += 1
        if str(abs(l[x + 2]))[-2:] == '11':
            k += 1
        if k == 2:
            if l[x] > sr and l[x + 1] > sr and l[x + 2] > sr:
                ct += 1
                mn = min(mn, l[x] + l[x + 1] + l[x + 2])
print(ct, mn)