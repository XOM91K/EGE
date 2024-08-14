l = [[int(d) for d in x.split()] for x in open('4.txt')]
ct = 0
for x in l:
    x.sort()
    chet = 0
    nechet = 0
    maxchet = 0
    for y in x:
        if y % 2 == 0:
            chet += 1
        else:
            nechet += 1
        # [22, 33, 33, 44, 55, 11, 80]
        if y % 2 == 0 and y > maxchet:
            maxchet = y

    if chet > 0 and nechet > 0 and chet % 2 == 0 and nechet % 2 != 0 and maxchet % 4 ==0:
        ct += 1
print(ct)