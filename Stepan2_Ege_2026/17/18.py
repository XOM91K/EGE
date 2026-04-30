l = [int(x) for x in open('18.txt')]
mn12 = min([d for d in l if d % 12 == 0 and d > 0])
mn = []
for x in range(len(l) - 2):
    k = 0
    if len(str(abs(l[x]))) == 5 and l[x] % 506 == 0:
        k += 1
    if len(str(abs(l[x + 1]))) == 5 and l[x + 1] % 506 == 0:
        k += 1
    if len(str(abs(l[x + 2]))) == 5 and l[x + 2] % 506 == 0:
        k += 1
    if k >= 1:
        dl100 = abs(l[x] * l[x + 1] * l[x + 2]) % 100
        if dl100 == mn12:
            mn.append(abs(l[x] + l[x + 1] + l[x + 2]))
print(len(mn), min(mn))