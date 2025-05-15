l = [[int(d) for d in x.split()] for x in open('15.txt')]
st1 = [x[0] for x in l]
st6 = [x[-1] for x in l]
ct = 0
for x in l:
    povt = [y for y in x if x.count(y) == 3]
    nepovt = [y for y in x if x.count(y) == 1]
    if len(povt) == 3 and len(nepovt) == 3:
        k = 0
        if st1.count(povt[0]) == 337:
            k += 1
        if st6.count(nepovt[0]) == 337 or st6.count(nepovt[1]) == 337 or st6.count(nepovt[2]) == 337:
            k += 1
        if k >= 1:
            ct += 1
print(ct)