num = -1
tr = []
ct = 0
while num != 0:
    num = int(input())
    tr.append(num)
    if len(tr) % 4 == 0:
        if (tr[0] * tr[2]) ** 0.5 == tr[1]:
            if (tr[1] * tr[3]) ** 0.5 == tr[2]:
                ct += 1
                tr.clear()
print(ct)