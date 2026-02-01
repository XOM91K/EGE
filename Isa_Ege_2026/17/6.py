l = [int(x) for x in open('6.txt')]
mx30 = max([x for x in l if str(x)[-2:] == '30'])
mx = []
for x in range(len(l) - 2):
    if len(str(abs(l[x]))) != 4 and len(str(abs(l[x + 1]))) != 4 and len(str(abs(l[x + 2]))) != 4:
        if l[x] + l[x + 1] + l[x + 2] > mx30:
            mx.append(l[x] + l[x + 1] + l[x + 2])
print(len(mx), max(mx))