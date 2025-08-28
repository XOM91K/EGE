l = [sorted([int(d) for d in x.split()]) for x in open('364.txt')]
ct = 0
for x in l:
    kr = [y for y in x if y % 3 == 0]
    if len(kr) == 3:
        if max(x)-min(x)<=sum(kr):
            ct+=1
print(ct)