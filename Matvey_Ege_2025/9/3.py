l = [[int(d) for d in x.split()] for x in open('3.txt')]
ct = 0
for x in l:
    ch = []
    nch = []
    for i in x:
        if i % 2 == 0:
            ch.append(i)
        else:
            nch.append(i)
    if len(ch) > 0 and len(nch) > 0:
        if len(ch) % 2 == 0 and len(nch) % 2 != 0:
            if max(ch) % 4 == 0:
                ct += 1
print(ct)