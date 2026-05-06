l = [int(x) for x in open("6.txt")]
mn = min([x for x in l if abs(x) % 100 == 25]) ** 2
mx = []
for i in range(len(l) - 2):
    k = 0
    if len(str(abs(l[i]))) == 4:
        k += 1
    if len(str(abs(l[i + 1]))) == 4:
        k += 1
    if len(str(abs(l[i + 2]))) == 4:
        k += 1
    if k >= 2 and (l[i] * l[i + 1] * l[i + 2]) <= mn:
        mx.append(l[i] * l[i + 1] * l[i + 2])
print(len(mx), max(mx))
