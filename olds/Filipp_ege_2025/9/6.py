li = [sorted([int(d) for d in x.split()]) for x in open('6.txt')]
ans = 0
for i in li:
    flag = 0
    summa = 0
    for j in i:
        if j % 3 == 0:
            flag += 1
            summa += j
    if flag == 3:
        if i[-1] - i[-0] <= summa:
            ans += 1
print(ans)