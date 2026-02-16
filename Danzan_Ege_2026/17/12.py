l = [int(x) for x in open('12.txt')]
mn17 = min([x for x in l if len(str(abs(x))) == 4 and x % 17 == 0]) ** 2
mn = []
for x in range(len(l) - 2):
    k = 0
    if len(str(abs(l[x]))) == 4 and str(l[x])[-2:] == '27':
        k += 1
    if len(str(abs(l[x + 1]))) == 4 and str(l[x + 1])[-2:] == '27':
        k += 1
    if len(str(abs(l[x + 2]))) == 4 and str(l[x + 2])[-2:] == '27':
        k += 1
    if k >= 1:
        if ((l[x])**2 + (l[x + 1])**2 + (l[x + 2])**2) <= mn17:
            mn.append(abs(l[x]) + abs(l[x + 1]) + abs(l[x + 2]))
print(len(mn), min(mn))