l = [sorted([int(d) for d in x.split()]) for x in open('10.txt')]
ct = 0
su = 0
for x in l:
    if len(set(x)) == 6:
        if x.count(x[2]) != 3 and x.count(x[4]) != 3 and x.count(x[5]) != 3:
            if x[0] != x[1]:
                ct += 8
                su += sum(x)
print(su / ct)