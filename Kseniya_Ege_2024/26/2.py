l = sorted([int(x) for x in open('2.txt')])
s = 100000
ct = 0
i = 0
j = len(l) - 1
last_element = 0
while s - l[i] >= 0:
    can = False
    if s - l[j] > 0:
        s -= l[j]
        ct += 1
        can = True
        last_element = l[j]
    j -= 1
    if can:
        if s - l[i] > 0:
            s -= l[i]
            i += 1
            ct += 1
            last_element = l[i]
print(ct, last_element)