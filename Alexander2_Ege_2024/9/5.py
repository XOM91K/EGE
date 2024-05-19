l = [[int(d) for d in x.split()] for x in open('5.txt')]
ct = 0
for x in l:
    x.sort()
    nm = ((x[0] + x[-1]) * 2)
    ls = ((x[1] + x[2] + x[3] + x[4] + x[5]) * 3)
    k = 0
    if len(set(x)) == 7:
        k += 1
    if nm <= ls:
        k += 1
    if k == 1:
        ct+=1
print(ct)