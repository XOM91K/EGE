l = [int(x) for x in open('2.txt')]
l = sorted(l)
print(l)
lt = 0
rt = len(l) - 1
yashik = 0
while lt < rt:
    if l[lt] + l[rt] == 100:
        yashik += 1
        rt -= 1
        lt += 1
    elif l[lt] + l[rt] > 100:
        rt -= 1
    elif l[lt] + l[rt] < 100:
        lt += 1
print(yashik)