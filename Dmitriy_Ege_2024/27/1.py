l = [int(x) for x in open('1.txt')]
mx_ct = 0
mx_sm = 0
l_sm = []
for x in range(len(l) - 1):
    l_sm.clear()
    l_sm.append(l[x])
    if sum(l_sm) % 113 == 0 and sum(l_sm) > mx_sm:
        mx_sm = sum(l_sm)
        mx_ct = max(mx_ct, len(l_sm))
        
    for y in range(x + 1, len(l)):
        l_sm.append(l[y])
        if sum(l_sm) % 113 == 0 and sum(l_sm) >= mx_sm:
            mx_sm = sum(l_sm)
            mx_ct = max(mx_ct, len(l_sm))
print(mx_ct)