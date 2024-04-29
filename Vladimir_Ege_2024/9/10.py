l = [sorted([int(d) for d in x.split()]) for x in open('10.txt')]
ct = 0
for x in l:
   if len(set(x)) == 5:
       if (x[0] + x[-1]) / 2 == x[2] and (x[1] + x[3]) / 2 == x[2]:
           ct += 1
           print(x)
print(ct)