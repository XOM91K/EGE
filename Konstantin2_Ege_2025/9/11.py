l = [[int(d) for d in x.split()] for x in open(r'C:\Users\Zarif\Downloads\912.txt')]
k = 0
for x in l:
    k += 1
    povt3 = []
    povt1 = []
    for y in x:
        if x.count(y) == 3:
            povt3.append(y)
        if x.count(y) == 1:
            povt1.append(y)
    if len(povt3) == 6 and len(povt1) == 1:
        if sum(povt3) / 6 < povt1[0]:
            print()
            print(k)