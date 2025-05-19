l = [int(x) for x in open('19.txt')]
c = []
e = []
for i in l:
    if len(str(abs(i))) == 4:
        if i % 17 == 0:
            c.append(i)
for x in range(len(l) - 2):
    if (len(str(abs(l[x]))) == 4 and str(l[x])[-2:] == '27') or (len(str(abs(l[x + 1]))) == 4 and str(l[x + 1])[-2:] == '27') or (len(str(abs(l[x + 2]))) == 4 and str(l[x + 2])[-2:] == '27'):
        if ((l[x] ** 2) + (l[x + 1] ** 2) + (l[x + 2] ** 2)) <= min(c) ** 2:
            e.append(abs(l[x]) + abs(l[x + 1]) + abs(l[x + 2]))
print(len(e), min(e))