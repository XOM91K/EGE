l = [int(x) for x in open('1.txt')]
l = sorted(l)[::-1]
matr = [l[0]]
for d in l:
    if matr[-1] - d >= 9:
        matr.append(d)
print(len(matr), matr[-1])
#1040 57