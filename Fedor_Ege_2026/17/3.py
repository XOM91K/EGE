l  = [int(x) for x in open('3.txt')]
sra = sum(l) / len(l)
xx = []
for x in range(len(l)- 1):
    if (l[x] % 7 == 0 and l[x] % 3 != 0 and l[x] % 11 != 0 and l[x] % 13 != 0) or (l[x+1] % 7 == 0 and l[x+1] % 3 != 0 and l[x+1] % 11 != 0 and l[x+1] % 13 != 0):
        if l[x] < sra or l[x + 1] < sra:
            xx.append(l[x]+l[x+1])
print(len(xx),min(xx))