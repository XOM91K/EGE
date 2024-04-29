l = [[int(d) for d in x.split()] for x in open('5.txt')]
ct = 0
for x in l:
    if len(set(x)) < len(x):
        if x.count(max(x)) == 1:
            povt = 0
            nepovt = 0
            for y in x:
                if x.count(y) == 1:
                    nepovt += y
                else:
                    povt += y
            if povt > nepovt:
                print(x)
                ct += 1
print(ct)