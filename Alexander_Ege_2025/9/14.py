ct=0
l = [[int(d) for d in x.split()]for x in open("14.txt")]
for x in l:
    k = [i for i in x if x.count(i) == 3]
    if len(k) == 3 and len(set(x)) == 4:
        povt = [i for i in x if x.count(i) > 1]
        nepovt = [i for i in x if x.count(i) == 1]
        if sum(nepovt) / len(nepovt) < sum(povt):
            ct += 1
print(ct)