l=[int(x) for x in open('166.txt')]
mn=[]
k151=[x for x in l if str(x)[-3:]=='151']
k151 = sum(k151) / len(k151)
mn = []
for x in range(len(l)-2):
    # 82
    # 959
    # -9206
    c4 = [x for x in [l[x], l[x + 1], l[x + 2]] if len(str(abs(x))) == 4]
    if 1 <= len(c4) <= 2:
        kr13 = [x for x in [l[x], l[x + 1], l[x + 2]] if x % 13 == 0]
        kr7 = [x for x in [l[x], l[x + 1], l[x + 2]] if x % 7 == 0]
        if len(kr13) > len(kr7):
            if l[x] > k151 and l[x + 1] > k151 and l[x + 2] > k151:
                mn.append(sum([l[x], l[x + 1], l[x + 2]]))
print(len(mn), min(mn))