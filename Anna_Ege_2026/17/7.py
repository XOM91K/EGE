l = [int(x) for x in open('7.txt')]
mx4 = max([x for x in l if len(str(x)) == 4]) ** 3
mx = []
for x in range(len(l) - 2):
    k = 0
    if str(l[x])[-1] == '3' or str(l[x])[-1] == '5':
        k += 1
    if str(l[x + 1])[-1] == '3' or str(l[x + 1])[-1] == '5':
        k += 1
    if str(l[x + 2])[-1] == '3' or str(l[x + 2])[-1] == '5':
        k += 1
    if k > 1:
        if l[x] * l[x + 1] * l[x + 2] <= mx4:
            mx.append(l[x] + l[x + 1] + l[x + 2])
print(len(mx), max(mx))