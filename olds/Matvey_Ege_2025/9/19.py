l = [[int(d) for d in x.split()] for x in open('19.txt')]
st1 = [x[0] for x in l]
st6 = [x[5] for x in l]
ct =0
for x in l:
    povt3 = [y for y in x if x.count(y) == 3]
    povt1 = [y for y in x if x.count(y) == 1]
    if len(povt3) == 3 and len(povt1) == 3:
        if st1.count(povt3[0]) == 337 or st6.count(povt1[0]) == 337 or st6.count(povt1[1]) == 337 or st6.count(povt1[2]) == 337:
            ct += 1
print(ct)