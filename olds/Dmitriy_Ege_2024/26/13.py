l = [[int(d) for d in x.split()] for x in open('13.txt')]
l = sorted(l)
start = 0
finish = 0
mx_time = 0
sm_time = 0
for x in l:
    if start <= x[0] <= finish:
        sm_time += max(finish, x[1]) - finish
        finish = max(finish, x[1])

    else:
        mx_time = max(mx_time, finish - start)
        sm_time += x[1] - x[0]
        start = x[0]
        finish = x[1]

print(sm_time, mx_time)