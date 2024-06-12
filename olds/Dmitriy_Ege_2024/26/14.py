l = sorted([[int(d) for d in x.split()] for x in open('14.txt')])
mx_pik = 0
ct_pik = 0
start = finish = 0
ct = 1
for x in l:
    if x[0] < finish:
        start = x[0]
        finish = min(finish, x[1])
        ct += 1
    else:
        mx_pik = max(mx_pik, ct)
        ct = 1
        start = x[0]
        finish = x[1]
print(mx_pik, ct)