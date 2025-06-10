def trio(num):
    ans = ""
    if num == 0:
        return "0"
    while num > 0:
        q = num % 3
        ans = str(q) + ans
        num = num // 3

    return ans

for n in range(1, 10000):
    r = trio(n)
    step_1 = 0
    for j in r:
        step_1 += int(j)
    if step_1 % 3 == 0:
        r = "20" + r
    else:
        r = "10" + r
    r = int(r, 3)
    if int(r) < 100:
        print(n)