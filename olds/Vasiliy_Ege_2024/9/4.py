l = [sorted([int(d) for d in x.split()]) for x in open('4.txt')]
ct = 0
k = 0
ct_str = 0
for x in l:
    k += 1
    if len(set(x)) == 5:
        if (x[0] * x[1]) * 2 <= x[2] + x[3] + x[4]:
            ct += k
            ct_str += 1
print(ct//ct_str)