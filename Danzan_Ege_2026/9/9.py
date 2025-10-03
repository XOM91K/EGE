l = [[int(d) for d in x.split()] for x in open('9.txt')]
ct = 0
for x in l:
    x = sorted(x)
    if x[3] < (x[0] + x[1] + x[2]):
        if (x[0] + x[1]) == (x[2] + x[3]) or (x[0] + x[2]) == (x[1] + x[3]) or (x[1] + x[2]) == (x[0] + x[3]):
            ct+=1
print(ct)