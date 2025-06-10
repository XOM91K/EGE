f = sorted([[int(a) for a in x.split()] for x in open('26.txt').readlines()])
pid = 0
mx_cnt = 0
mx_id = 0
cnt = 1
pt = -10
for s in f:
    id = s[0]
    t = s[1]
    if id == pid:
        if abs(pt-t) == 2:
            cnt += 1

        pt = t
    else:
        if cnt > mx_cnt:
            mx_id = pid
            mx_cnt = cnt
        pid = id
        cnt = 1
        pt = t

print(mx_id, mx_cnt)