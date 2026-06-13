l = [int(x) for x in open('17.txt')]
mn99 = min([d for d in l if d > 0 and str(d)[-2:] == '99'])
print(mn99)
mn = []
for x in range(len(l) - 2):
    k = 0
    if len(str(abs(l[x]))) == 3:
        k += 1
    if len(str(abs(l[x + 1]))) == 3:
        k += 1
    if len(str(abs(l[x + 2]))) == 3:
        k += 1
    if k >= 2:
        if l[x] + l[x + 1] + l[x + 2] >= mn99:
            mn.append(l[x] + l[x + 1] + l[x + 2])
print(len(mn), min(mn))