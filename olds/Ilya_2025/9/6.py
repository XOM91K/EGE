l = [[int(d) for d in x.split()] for x in open('6.txt')]
all_num = []
for x in l:
    for y in x:
        all_num.append(y)
ct = 0
for x in l:
    for y in x:
        if x.count(y) == 1 and all_num.count(y) == 51:
            ct += 1
            print(y, x)
print(ct)