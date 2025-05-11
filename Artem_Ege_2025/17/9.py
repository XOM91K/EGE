a = [int(x) for x in open('9.txt')]
mn = min([x for x in a if str(x)[-2:] == '25'])
b = []
for i in range(len(a) - 2):
    k = 0
    if len(str(abs(a[i]))) == 4:
        k += 1
    if len(str(abs(a[i + 1]))) == 4:
        k += 1
    if len(str(abs(a[i + 2]))) == 4:
        k += 1
    if k >= 2:
        if (a[i] * a[i + 1] * a[i + 2]) <= mn * mn:
            b.append(a[i] * a[i + 1] * a[i + 2])
print(len(b), max(b))
