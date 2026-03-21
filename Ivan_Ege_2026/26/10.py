l = [[int(d) for d in x.split()] for x in open('10.txt')]
ot = [0] * 1440
print(ot)
print(l)
for x in l:
    for i in range(x[0], x[1] + 1):
        ot[i] += 1
print(ot)
print(max(ot))
for x in range(len(ot)):
    if ot[x] == max(ot):
        print(x)