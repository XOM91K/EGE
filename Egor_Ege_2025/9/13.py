l = [[int(d) for d in x.split()] for x in open('13.txt')]
st1 = [x[0] for x in l]
st6 = [x[-1] for x in l]
ct = 0
for x in l:
    a = [i for i in x if x.count(i) == 3]
    b = [i for i in x if x.count(i) == 1]
    if len(a) == 3 and len(b) == 3:
        if st1.count(a[0]) == 337 or st6.count(b[0]) == 337 or st6.count(b[1]) == 337  or st6.count(b[2]) == 337:
            ct += 1
print(ct)