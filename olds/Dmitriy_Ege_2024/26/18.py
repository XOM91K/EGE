l = sorted([[int(d) for d in x.split()] for x in open('18.txt')])
k = [0] * 210
ct_pass = 0
for x in l:
    for y in range(len(k)):
        if x[0] > k[y]:
            ct_pass += 1
            k[y] = x[1]
            print(y + 1)
            break
print(ct_pass)