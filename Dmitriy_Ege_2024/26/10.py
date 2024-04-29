l = sorted([int(x) for x in open('10.txt')])
i = 0
j = len(l) - 1
yashik = 0
while i < j:
    if l[i] + l[j] == 100:
        yashik += 1
        i += 1
        j -= 1
    elif l[i] + l[j] > 100:
        j -= 1
    elif l[i] + l[j] < 100:
        i += 1
print(yashik)