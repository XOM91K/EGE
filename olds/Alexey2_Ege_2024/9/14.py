l = [sorted([int(d) for d in x.split()]) for x in open('14.txt')]
# sorted() обязательно!
ct = 0
for x in l:
    if x[-1] < x[0] + x[1] + x[2]:
        if len(set(x)) == 4: # или len(set(x)) == len(x)
            ct += 1
print(ct)