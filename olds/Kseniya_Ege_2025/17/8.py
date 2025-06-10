l = [int(x) for x in open('8.txt')]
mnsm = []
#sr28 = sum([x for x in l if str(x)[-2:] == '28']) / len([x for x in l if str(x)[-2:] == '28'])
sr28 = [x for x in l if str(x)[-2:] == '28']
sr28 = sum(sr28) / len(sr28)
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
            if l[x] > sr28 and l[x + 1] > sr28 and l[x + 2] > sr28:
                mnsm.append(l[x] + l[x + 1] + l[x + 2])
print(len(mnsm), min(mnsm))