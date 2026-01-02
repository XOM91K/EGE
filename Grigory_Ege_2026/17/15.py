l = [int(x) for x in open('15.txt')]
kv = len(l) ** 2
mx = []
for x in range(len(l) - 2):
    d = sorted([l[x], l[x + 1], l[x + 2]])
    if d[-1] + d[-2] > kv:
        if len(str(abs(d[-1]))) == 4 and len(str(abs(d[-2]))) == 4:
            if str(abs(d[-1]))[-1] == '3' and str(abs(d[-2]))[-1] == '3':
                mx.append(abs(l[x] + l[x + 1] + l[x + 2]))
print(len(mx), max(mx))
