#только 2 ящика по 100 монет 10 + 90 и 66 + 34. Ответ: 2.
#на полякове №2643
l = sorted([int(x) for x in open('3.txt')])
i = 0
j = len(l) - 1
ct_yash = 0
while i < j:
    if l[i] + l[j] > 100:
        j -= 1
    elif l[i] + l[j] == 100:
        ct_yash += 1
        j -= 1
        i += 1
    elif l[i] + l[j] < 100:
        i += 1
print(ct_yash)