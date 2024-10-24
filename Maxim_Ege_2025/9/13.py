v = [sorted([int(d) for d in x.split()]) for x in open('13.txt')]
ct = 0
for x in v:
   if x.count(x[0]) == 3 or x.count(x[1]) == 3 or x.count(x[2]) == 3 or x.count(x[3]) == 3 or x.count(x[4]) == 3 or x.count(x[5]) == 3 or x.count(x[6]) == 3:
       if len(set(x)) == 3:
           ch = 0
           nch = 0
           for y in x[:4]:
               if y % 2 == 0:
                   ch += 1
               else:
                   nch += 1
           if ch == 2 and nch == 2:
               ct += sum(x)
print(ct)