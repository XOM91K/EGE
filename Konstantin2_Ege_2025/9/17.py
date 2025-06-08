l = [[int(d) for d in x.split()] for x in open('17.txt')]
ct = 0
k = 0
for x in l:
    p = [v for v in x if x.count(v) == 3]
    np = [v for v in x if x.count(v) == 1]
    if len(p) == 3 and len(np) == 3:
        st1 = 0
        st6_1 = 0
        st6_2 = 0
        st6_3 = 0
        for y in l:
            if y[0] == p[0]:
                st1 += 1
            if y[5] == np[0]:
                st6_1 += 1
            if y[5] == np[1]:
                st6_2 += 1
            if y[5] == np[2]:
                st6_3 += 1
        if st1 == 337 or (st6_1 == 337 or st6_2 == 337 or st6_3 == 337):
                ct +=1
print(ct)