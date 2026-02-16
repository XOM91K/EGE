l = [int(x) for x in open('4.txt')]
l = sorted(l)
i = 0
j = len(l) - 1
yash = 0
while i < j:
    if l[i] + l[j] == 100:
        yash += 1
        i += 1
        j -= 1
    elif l[i] + l[j] < 100:
        i += 1
    else:
        j -= 1

print(yash)
