l = [sorted([int(d) for d in x.split()]) for x in open('1.txt')]
# '37\t83\t24\t19\t37\n' => [37, 83, 24, 19, 37]
ct = 0
for x in l:
    # [1, 2, 3, 4, 1]
    if len(set(x)) == 4:
        if (x[-1] + x[0]) ** 2 < x[1] ** 2 + x[2] ** 2 + x[3] ** 2:
            ct += 1
print(ct)