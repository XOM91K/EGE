l = [int(x) for x in open('4.txt')]
mn25 = min([y for y in l if str(y)[-2:] == '25']) ** 2
pr = []
for x in range(len(l) - 2):
    k = 0
    if len(str(abs(l[x]))) == 4:
        k += 1
    if len(str(abs(l[x + 1]))) == 4:
        k += 1
    if len(str(abs(l[x + 2]))) == 4:
        k += 1
    if k >= 2:
        if l[x] * l[x + 1] * l[x + 2] <= mn25:
            print(l[x] , l[x + 1], l[x + 2])
            pr.append(l[x] * l[x + 1] * l[x + 2])
print(len(pr), max(pr))