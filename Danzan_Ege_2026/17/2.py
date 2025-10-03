l = [int(x) for x in open('2.txt')]
mn41 = min([x for x in l if x % 41 == 0 and x > 0])
mx = []
for x in range(len(l) - 1):
    if l[x] != l[x + 1]:
        if abs(l[x] - l[x + 1]) % mn41 == 0:
            mx.append(l[x] + l[x + 1])
print(len(mx), max(mx))