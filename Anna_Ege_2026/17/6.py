l = [int(x) for x in open('6.txt')]
mx13 = max([x for x in l if str(x)[-2:] == '13'])
mx = []
for x in range(len(l) - 2):
    k = 0
    if len(str(l[x])) == 3:
        k += 1
    if len(str(l[x + 1])) == 3:
        k += 1
    if len(str(l[x + 2])) == 3:
        k += 1
    if k == 2:
        if l[x] + l[x + 1] + l[x + 2] <= mx13:
            mx.append(l[x] + l[x + 1] + l[x + 2])

print(len(mx), max(mx))