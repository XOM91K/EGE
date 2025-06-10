def second(lst):
    res = []
    for item in lst:
        if item % 3 == 0:
            res.append('3')
        elif item % 7 == 0:
            res.append('7')
    return res


l = [int(x) for x in open('4.txt')]
newlst = [x for x in l if str(x)[-3:] == '652']
smmxmn = max(newlst) + min(newlst)
cnt = mx = 0
for i in range(len(l) - 3):
    lst = [l[i], l[i+1], l[i+2], l[i+3]]
    frst = [len(str(l[i])), len(str(l[i+1])), len(str(l[i+2])), len(str(l[i+3]))].count(5) > [len(str(l[i])), len(str(l[i+1])), len(str(l[i+2])), len(str(l[i+3]))].count(4)
    scnd = second(lst).count('3') == second(lst).count('7')

    thrd = sum(lst) > smmxmn * 2
    if frst and scnd and thrd:
        cnt += 1
        if mx < sum(lst):
            mx = sum(lst)

print(cnt, mx)