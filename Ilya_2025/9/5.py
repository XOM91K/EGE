l = [[int(d) for d in x.split()] for x in open('5.txt')]
ct = 0
for x in l:
    if len(set(x)) == 5:
        if len([d for d in x if d % 2 == 0]) > len([d for d in x if d % 2 != 0]):
            if sum([d for d in x if d % 2 == 0]) < sum([d for d in x if d % 2 != 0]):
                ct += 1
print(ct)