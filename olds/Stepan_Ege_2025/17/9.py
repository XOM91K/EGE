l = [int(x) for x in open('9.txt')]
mn17 = min([y for y in l if len(str(abs(y))) == 4 and y % 17 == 0])
mn = []
for x in range(len(l) - 2):
    if (len(str(abs(l[x]))) == 4 and str(abs(l[x]))[-2:] == '27') or (len(str(abs(l[x + 1]))) == 4 and str(abs(l[x + 1]))[-2:] == '27') or (len(str(abs(l[x + 2]))) == 4 and str(abs(l[x + 2]))[-2:] == '27'):
        if (l[x]** 2 + l[x + 1] ** 2 + l[x + 2] ** 2) <= mn17 ** 2:
            mn.append(abs(l[x]) + abs(l[x + 1]) + abs(l[x + 2]))
print(len(mn), min(mn))