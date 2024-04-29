l = [sorted([int(d) for d in x.split()]) for x in open(r'C:\Users\Zarif\PycharmProjects\EGE\Sergey_Ege_2025\9\2.txt')]
ct = 0
for x in l:
    if (x[-1] + x[0]) ** 2 < x[1] ** 2 + x[2] ** 2 + x[3] ** 2:
        if len(set(x)) == 4:
            ct += 1
print(ct)