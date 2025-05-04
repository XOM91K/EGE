l = [int(x) for x in open('6.txt')]
sr28 = [x for x in l if str(x)[-2:] == '28']
sr28 = sum(sr28) / len(sr28)
mn = []
for x in range(len(l) - 2):
    if len(str(abs(l[x]))) == 4 or  len(str(abs(l[x + 1]))) == 4 or  len(str(abs(l[x + 2]))) == 4:
        k = 0
        if str(abs(l[x]))[-2:] == '11':
            k += 1
        if str(abs(l[x + 1]))[-2:] == '11':
            k += 1
        if str(abs(l[x + 2]))[-2:] == '11':
            k += 1
        if k == 2:
            if l[x] > sr28 and l[x + 1] > sr28 and l[x + 2] > sr28:
                mn.append(l[x] + l[x + 1] + l[x + 2])
print(len(mn), min(mn))