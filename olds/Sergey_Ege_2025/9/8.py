l = [sorted([int(d) for d in x.split()]) for x in open("8.txt")]
ct = 0
for x in l:
  if len(x)-2 == len(set(x)) and x.count(x[2]) != 3 and x.count(x[3]) != 3:
    if (x[-1] + x[0])/2 < (x[1] + x[2] + x[3] + x[4])/4:
        print(x)
        ct += 1
print(ct)