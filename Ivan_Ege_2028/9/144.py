l = [[int(d) for d in x.split()] for x in open('144.txt')]
ct = 0
for x in l:
    povt1 = [d for d in x if x.count(d) == 1]
    povt2 = [d for d in x if x.count(d) == 2]
    chet = [d for d in x if d % 2 == 0]
    nechet = [d for d in x if d % 2 != 0]
    k = 0
    if (len(povt1) == 3 and len(povt2) == 2):
        k += 1
    if sum(nechet) > sum(chet):
        k += 1
    if k == 1:
        print(x)
        ct += 1
print(ct)