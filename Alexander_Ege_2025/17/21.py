l = [int(x) for x in open('21.txt')]
mx5 = max([i for i in l if str(i)[-1] == '5'])
mx = []
for x in range(len(l) - 2):
    k = 0
    if len(str(abs(l[x]))) == 5:
        k += 1
    if len(str(abs(l[x + 1]))) == 5:
        k += 1
    if len(str(abs(l[x + 2]))) == 5:
        k += 1
    if k == 2:
        if l[x] + l[x + 1] + l[x + 2] > mx5:
            mx.append(l[x] + l[x + 1] + l[x + 2])
print(len(mx), max(mx))