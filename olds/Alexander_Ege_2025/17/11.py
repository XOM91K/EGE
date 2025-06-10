l = [int(x) for x in open("11.txt")]
z1 = max([i for i in l if len(str(abs(i))) == 4 and str(i)[-1] == "1"])
min2 = min([i for i in l if len(str(abs(i))) == 2])
mx = []
for x in range(len(l) - 2):
    k = 0
    if l[x] > min2 ** 2:
        k += 1
    if l[x + 1] > min2 ** 2:
        k += 1
    if l[x + 2] > min2 ** 2:
        k += 1
    if k == 2:
        if (abs(l[x]) * abs(l[x + 1]) * abs(l[x + 2])) % z1 == 0:
            mx.append(abs(l[x]) + abs(l[x + 1]) + abs(l[x + 2]))
print(len(mx), max(mx))