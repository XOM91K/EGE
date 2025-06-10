l = [int(x) for x in open('13.txt')]
l2 = []
ct = 0
mn = 1000000
for x in l:
    if str(x)[-2:] == '28':
        l2.append(x)
sr = sum(l2) / len(l2)
for x in range(len(l) - 2):
    if len(str(abs(l[x]))) == 4 or len(str(abs(l[x + 1]))) == 4 or len(str(abs(l[x + 2]))) == 4:
        k = 0
        if str(l[x])[-2:] == '11':
            k += 1
        if str(l[x + 1])[-2:] == '11':
            k += 1
        if str(l[x + 2])[-2:] == '11':
            k += 1
        if k == 2:
            if l[x] > sr and l[x + 1] > sr and l[x + 2] > sr:
                ct += 1
                mn = min(mn, l[x] + l[x + 1] + l[x + 2])
print(ct, mn)