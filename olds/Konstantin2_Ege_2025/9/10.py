l = [sorted([int(d) for d in x.split()]) for x in open("10.txt")]
ct =0
for x in l:
    ch = 0
    nch = 0
    mx_ch = 0
    for y in range(len(x)):
        if x[y] % 2 == 0:
            ch += 1
            mx_ch = max(mx_ch, x[y])
        else:
            nch += 1
    if ch > 0 and nch > 0 and ch % 2 == 0 and nch % 2 != 0:
        if mx_ch % 4 == 0:
            ct +=1
            print(ct)