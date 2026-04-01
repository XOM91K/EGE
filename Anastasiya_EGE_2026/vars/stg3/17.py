l = [int(x) for x in open('17.txt')]
mx = []
mx70 = max([d for d in l if str(d)[-2:] == '70'])
for x in range(len(l) - 2):
    if l[x] > 0 and l[x + 1] > 0 and l[x + 2] > 0:
        if l[x] + l[x + 1]  + l[x + 2] <= mx70:
            mx.append(l[x] + l[x + 1]  + l[x + 2])
print(len(mx), max(mx))