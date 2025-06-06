a = [[int(j) for j in i.split()]for i in open("12.txt")]
count = 0
for i in a:
    p = [j for j in i if i.count(j) == 3]
    np = [j for j in i if i.count(j) == 1]
    if len(p) == 3 and len(np) == 3:
        k = 0
        k1 = 0
        k2 = 0
        k3 = 0
        for j in a:
            if j[0] == p[0]:
                k += 1
            if j[-1] == np[0]:
                k1 += 1
            if j[-1] == np[1]:
                k2 += 1
            if j[-1] == np[2]:
                k3 += 1
        if k1 == 337 or k == 337 or k2 == 337 or k3 == 337:
            count += 1
print(count)