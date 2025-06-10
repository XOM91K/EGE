l= [sorted([int(d) for d in x.split()]) for x in open('14.txt')]
ct = 0
for x in l:
    min_hj = abs(sum([y for y in x if y < 0]))
    max_hj = sum([y for y in x if y > 0])
    if len(set(x)) == 5:
        if min_hj > max_hj:
            ct += 1
print(ct)