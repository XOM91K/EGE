l = [int(x) for x in open('2.txt')]
l = sorted(l)[::-1]
matr = [l[0]]
for x in l:
    if abs(x - matr[-1]) >= 9:
        matr.append(x)
print(len(matr), matr[-1])