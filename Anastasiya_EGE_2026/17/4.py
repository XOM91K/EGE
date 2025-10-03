l = [int(x) for x in open('4.txt')]
mn41 = min([y for y in l if y % 41 == 0 and y > 0])
mx = []
for x in range(len(l) - 1):
    if l[x] != l[x + 1] and abs(l[x] - l[x + 1]) % mn41 == 0:
        mx.append(l[x] + l[x + 1])
print(len(mx), max(mx))
