l = [int(x) for x in open('1.txt')]
mx = []
sr = sum(l) / len(l)
for x in range(len(l) - 1):
    if l[x] < sr and l[x + 1] < sr:
        if l[x] % 10 == 9 or l[x + 1] % 10 == 9:
            mx.append(l[x] + l[x + 1])
print(len(mx), max(mx))