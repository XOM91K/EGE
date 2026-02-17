l = [[int(d) for d in x.split()] for x in open('8.txt')]
ct = 0
for x in l:
    ch = [d for d in x if d % 2 == 0]
    nch = [d for d in x if d % 2 != 0]
    if len(ch) > 0 and len(nch) > 0:
        if len(ch) % 2 == 0 and len(nch) % 2 != 0:
            if max(ch) % 4 == 0:
                ct += 1
print(ct)