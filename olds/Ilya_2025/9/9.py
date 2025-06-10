l = [[int(d) for d in x.split()] for x in open('9.txt')]
ct = 0
for x in l:
    if len(set(x)) == 4:
        x.sort()
        if x.count(x[2]) == 3 or x.count(x[3]) == 3:
            pvt3 = 0
            if x.count(x[2]) == 3:
                pvt3 = x[2]
            else:
                pvt3 = x[3]
            if (sum(x) - pvt3 * 3) / 3 < pvt3 * 3:
                ct += 1
print(ct)