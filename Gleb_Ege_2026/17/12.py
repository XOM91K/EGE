l = [int(x) for x in open('12.txt')]
mx = []
m = min(l)
for x in range(len(l) - 1):
    if ((l[x] % 77) * (l[x + 1] % 77)) == m ** 2:
        print(l[x])
        mx.append(l[x] * l[x + 1])
print(len(mx), min(mx))