l = [int(x) for x in open('3.txt')]
sr = [x for x in l if str(x)[-2:] == '28']
sr = sum(sr) / len(sr)
mn = []
for x in range(len(l) - 2):
    k = 0
    if len(str(abs(l[x]))) == 4:
        k += 1
    if len(str(abs(l[x + 1]))) == 4:
        k += 1
    if len(str(abs(l[x + 2]))) == 4:
        k += 1
    if k >= 1:
        k = 0
        if str(l[x])[-2:] == '11':
            k += 1
        if str(l[x + 1])[-2:] == '11':
            k += 1
        if str(l[x + 2])[-2:] == '11':
            k += 1
        if k == 2:
            if l[x] > sr and l[x + 1] > sr and l[x + 2] > sr:
                mn.append(l[x] + l[x + 1] + l[x + 2])

print(len(mn), min(mn))