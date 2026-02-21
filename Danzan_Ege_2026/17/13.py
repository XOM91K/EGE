l = [int(x) for x in open('13.txt')]
minmax = min(l) - max(l)
mx = []
for x in range(len(l) - 1):
    for y in range(x + 1, len(l)):
        k = 0
        if len(str(abs(l[x]))) == 5 and l[x] < 0 and l[x] % 46 == 0:
            k+=1
        if len(str(abs(l[y]))) == 5 and l[y] < 0 and l[y] % 46 == 0:
            k+=1
        if k == 1:
            if ((l[x] - l[y])**2) % minmax == 0:
                mx.append((l[x] - l[y])**2)
print(len(mx), max(mx))