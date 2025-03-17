l = [[int(d) for d in x.split()]for x in open('4.txt')]
k = 0
for x in l:
    if len(set(x)) == 5:
        x.sort()
        if (x[0] + x[-1]) / 2 == (x[1] + x[-2])/2 == x[2]:
            k += 1
print(k)