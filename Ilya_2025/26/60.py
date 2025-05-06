a = sorted([[int(i) for i in x.split()] for x in open('2.txt')])
ct_2 = 0
ct_y = 0
tek_1 = []
tek_2 = []
for i in a:
    while len(tek_1) > 0 and tek_1[0] <= i[0]:
        del tek_1[0]
    while len(tek_2) > 0 and tek_2[0] <= i[0]:
        del tek_2[0]
    if i[2] == 1 and len(tek_1) < 14:
        if tek_1 != []:
            tek_1.append(max(tek_1[-1], i[0]) + i[1])
        else:
            tek_1.append(i[0] + i[1])
    elif i[2] == 1:
        ct_y += 1
    if i[2] == 2 and len(tek_2) < 14:
        ct_2 += 1
        if tek_2 != []:
            tek_2.append(max(tek_2[-1], i[0]) + i[1])
        else:
            tek_2.append(i[0] + i[1])
    elif i[2] == 2:
        ct_y += 1
    if i[2] == 0:
        if len(tek_2) < len(tek_1) and len(tek_2) < 14:
            if tek_2 != []:
                tek_2.append(max(tek_2[-1], i[0]) + i[1])
            else:
                tek_2.append(i[0] + i[1])
            ct_2 += 1
        elif len(tek_2) > len(tek_1) and len(tek_1) < 14:
            if tek_1 != []:
                tek_1.append(max(tek_1[-1], i[0]) + i[1])
            else:
                tek_1.append(i[0] + i[1])
        elif len(tek_2) == len(tek_1) and len(tek_2) < 14:
            if tek_1 != []:
                tek_1.append(max(tek_1[-1], i[0]) + i[1])
            else:
                tek_1.append(i[0] + i[1])
        else:
            ct_y += 1
print(ct_2, ct_y)
