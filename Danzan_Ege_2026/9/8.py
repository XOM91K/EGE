l = [[int(d) for d in x.split()] for x in open('8.txt')]
ct = 0
for x in l:
    x = sorted(x)
    kr3 = [d for d in x if d % 3 == 0]
    if len(kr3) == 3:
        if (x[5] - x[0]) <= sum(kr3):
            ct+=1
print(ct)