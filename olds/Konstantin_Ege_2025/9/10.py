l = [[int(d) for d in x.split()] for x in open('10.txt')]
ct = 0
for x in l:
    if len(set(x)) < 6:
        if x.count(max(x)) == 1:
            povt = 0
            # x = [22, 22, 1, 2, 33, 33]
            for y in x:
                if x.count(y) > 1:
                    povt += y
            if povt < max(x):
                ct += 1
print(ct)