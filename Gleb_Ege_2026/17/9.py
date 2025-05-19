l = [int(x) for x in open('9.txt')]
mn = []
na28 = [x for x in l if str(x)[-2:] == '28']
sr_na28 = sum(na28) / len(na28)
for x in range(len(l) - 2):
    k = 0
    if len(str(abs(l[x]))) == 4 or len(str(abs(l[x + 1]))) == 4 or len(str(abs(l[x + 2]))) == 4:
        if l[x] > sr_na28 and l[x + 1] > sr_na28 and l[x + 2] > sr_na28:
            if str(l[x])[-2:] == '11':
                k += 1
            if str(l[x + 1])[-2:] == '11':
                k += 1
            if str(l[x + 2])[-2:] == '11':
                k += 1
            if k == 2:
                mn.append(l[x] + l[x + 1] + l[x + 2])
print(len(mn), min(mn))