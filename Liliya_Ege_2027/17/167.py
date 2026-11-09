l = [int(x) for x in open('167.txt')]
sr28 = [d for d in l if str(d)[-2:] == '28']
mn = []
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
                mn.append(l[x] + l[x + 1] + l[x + 2])
print(len(mn), min(mn))