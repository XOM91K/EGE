l = [[int(d) for d in x.split()]for x in open('8.txt')]
ct = 0
povt = []
for x in l:
    #if len(set(x)) == 4: # 44 44 44 22 23 25  1 2 3 4 5
    povt2 = [d for d in x if x.count(d) == 2]
    povt1 = [d for d in x if x.count(d) == 1]
    if len(povt2) == 4 and len(povt1) == 2:
        if sum(set(povt2)) < sum(povt1):
            ct += 1
print(ct)