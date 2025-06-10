l = [[int(d) for d in x.split()] for x in open('371.txt')]
ct = 0
for x in l:
    ch = [y for y in x if y % 2 == 0]
    nch = [y for y in x if y % 2 != 0]
    if len(ch) > 0 and len(nch) > 0:
        if len(ch) % 2 == 0 and len(nch) % 2 != 0:
            if max(ch) % 4 == 0:
                ct += 1
print(ct)