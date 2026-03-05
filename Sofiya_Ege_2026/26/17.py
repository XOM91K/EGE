l = [[int(d) for d in x.split()] for x in open('17.txt')]
l = sorted(l, key=lambda d: (d[-1], d[0]))
for x in l:
    print(x)
time_zal = l[0][1]
z = [l[0]]
for x in l:
    if len(z) % 3 == 0:
        per = 10
    else:
        per = 0
    if x[0] >= time_zal + per:
        time_zal = x[1]
        z.append(x)
print(len(z))
k = 0
for x in z:
    k += 1
    print(k, x)
for x in l:
    if x[0] > 1246:
        print(x)