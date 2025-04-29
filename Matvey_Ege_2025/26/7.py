l = [[int(d) for d in x.split()] for x in open('7.txt')]
l = sorted(l, key=lambda d: d[1])
lekcii = []
time_zal = 0

for x in l:
    if x[0] >= time_zal:
        lekcii.append(x)
        if len(lekcii) % 3 == 0:
            time_zal = x[1] + 10
        else:
            time_zal = x[1]
print(len(lekcii))
print(lekcii)