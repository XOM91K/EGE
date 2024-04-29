l = [int(x) for x in open('7.txt')]
otv = []
ct = 0
for o in l:
    for x in range(len(l) - 1):
        if (len(str(l[x])) == 2 and len(str(l[x + 1])) != 2) or (len(str(l[x])) != 2 and len(str(l[x + 1])) == 2):
            if o <= (l[x] + l[x + 1]):
                break
    else:
        ct += 1
        otv.append(o)
print(ct, min(otv))