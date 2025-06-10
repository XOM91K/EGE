l = [sorted([int(d) for d in x.split()]) for x in open('10.txt')]
ct = 0
for x in l:
    usl = 0
    if len(set(x)) == 4:
        usl += 1
    chet = 0
    nechet = 0
    for y in x:
        if y % 2 == 0:
            chet += y
        else:
            nechet += y
    if nechet > chet:
        usl += 1
    if usl == 1:
        ct += 1
print(ct)