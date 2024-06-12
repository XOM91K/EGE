l = [[int(d) for d in x.split()] for x in open('2.txt')]
k = 0
for x in l:
    k += 1
    if len(set(x)) == 5:
        povt = sum(x) - sum(set(x))
        sr = (sum(x) - 2 * povt) / 4
        if povt >= sr:
            print(k, x)
print(k)