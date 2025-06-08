l = [int(x) for x in open('17_0.txt')]
mn4 = min([x for x in l if len(str(abs(x))) == 4 and sum(map(int, str(abs(x)))) == 21 and x > 0])
mx = []
for x in range(len(l) - 2):
    k = 0
    if len(str(abs(l[x]))) == 4 and sum(map(int, str(abs(l[x])))) == 15:
        k += 1
    if len(str(abs(l[x + 1]))) == 4 and sum(map(int, str(abs(l[x + 1])))) == 15:
        k += 1
    if len(str(abs(l[x + 2]))) == 4 and sum(map(int, str(abs(l[x + 2])))) == 15:
        k += 1
    if k == 2:
        if 98 * (l[x] + l[x + 1] + l[x + 2]) >= mn4 ** 2:
            mx.append(l[x] + l[x + 1] + l[x + 2])
print(len(mx), max(mx))