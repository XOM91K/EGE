l = [[int(d) for d in x.split()] for x in open('10.txt')]
l = sorted(l, key=sum)
k = 8
ct = []
time_end = 0
for x in l:
    if x[0] >= time_end:
        time_end = sum(x)
        ct.append(x)
mx_rzn = 10 ** 10
print(ct)
for i in range(len(l) - 1, -1, -1):
    if l[i][0] > sum(ct[-2]):
        mx_rzn = min(mx_rzn, l[i][0])
print(len(ct) * k, mx_rzn)