l = [[int(d) for d in x.split()] for x in open('4.txt')]
l = sorted(l)
finish = 0
print(l)
old_sum = l[0][0]
new_sum = l[0][1]
sum_t = 0
can = False
for x in l:
    if x[0] > finish:
        if can:
            print(new_sum-old_sum)
            old_sum = new_sum
        can = True
        sum_t += x[1] - x[0]
    elif x[1] <= finish:

        pass
    else:
        new_sum = max(new_sum, x[1])
        sum_t += x[1] - finish
    finish = max(finish, x[1])
print(sum_t)