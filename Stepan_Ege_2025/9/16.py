l = [sorted([int(d) for d in x.split()]) for x in open('16.txt')]
ct = 0
for x in l:
    ok5 = 0
    if (x[4] + x[3]) * 2 > (x[0] + x[1] + x[2]) * 3:
        for y in range(len(x)):
            if str(x[y])[-1] == '5':
                ok5 += 1
        if ok5 >= 2:
            print(x, ok5)
            ct += 1
print(ct)
# d = [55, 99,11, 22]
# for x in d:
#     print(x)
# for x in range(len(d)):
#     print(d[x])