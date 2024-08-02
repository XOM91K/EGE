l = sorted([[int(d) for d in x.split()] for x in open('6.txt')])
sm_time = l[0][1] - l[0][0]
start_f = l[0][0]
end_f = l[0][1]
del l[0]
sp = []
ln_time = sm_time
for i in l:
    if i[0] > end_f:
        sp.append(ln_time)
        ln_time = i[1] - i[0]
        start_f = i[0]
        end_f = i[1]
        sm_time += end_f - start_f
    elif i[0] == end_f:
        end_f = i[1]
        ln_time += i[1] - i[0]
        sm_time += i[1] - i[0]
    else:
        if i[1] > end_f:
            ln_time += i[1] - end_f
            sm_time += i[1] - end_f
            end_f = i[1]
sp.append(ln_time)
print(sm_time, max(sp))