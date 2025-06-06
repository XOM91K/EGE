def sum_cif(d):
    s = 0
    for i in str(d):
        s += int(i)
    return s % 2 == 0
l = [[int(d) for d in x.split()] for x in open('13.txt')]
k = 0
for x in l:
    k += 1
    if x == sorted(x):
        r = [i for i in x if x.count(i) > 1 and sum_cif(i)]
        if len(r) > 0:
            print(k)