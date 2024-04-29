l = sorted([[int(d) for d in x.split()] for x in open('17.txt')])
w1 = [0, []]
w2 = [0, []]
cnt_neob =  0
for x in l:
    if x[-1] == 1:
        if len(w1[1]) >= 14:
            cnt_neob += 1
            continue
        if x[0] >= w1[0] and len(w1[1]) == 0:
            w1[0] = x[0] + x[1]
        elif x[0] >= w1[0] and len(w1[1]) > 0:
            w1[0] = w1[0] + w1[1][0]
            del w1[1][0]
        else:
            w1[1].append(x[1])
    elif x[-1] == 2:
        if len(w2[1]) >= 14:
            cnt_neob += 1
            continue
        if x[0] >= w2[0] and len(w2[1]) == 0:
            w2[0] = x[0] + x[1]
        elif x[0] >= w2[0] and len(w2[1]) > 0:
            w2[0] = w2[0] + w2[1][0]
            del w2[1][0]
        else:
            w2[1].append(x[1])
    elif x[-1] == 0:
        if len(w1[1]) < len(w2[1]):
            if len(w1[1]) >= 14:
                cnt_neob += 1
                continue
            if x[0] >= w1[0] and len(w1[1]) == 0:
                w1[0] = x[0] + x[1]
            elif x[0] >= w1[0] and len(w1[1]) > 0:
                w1[0] = w1[0] + w1[1][0]
                del w1[1][0]
            else:
                w1[1].append(x[1])
        else:
            if len(w2[1]) >= 14:
                cnt_neob += 1
                continue
            if x[0] >= w2[0] and len(w2[1]) == 0:
                w2[0] = x[0] + x[1]
            elif x[0] >= w2[0] and len(w2[1]) > 0:
                w2[0] = w2[0] + w2[1][0]
                del w2[1][0]
            else:
                w2[1].append(x[1])
print(cnt_neob)