l = sorted([int(x) for x in open(r'C:\Users\Zarif\PycharmProjects\EGE\Alexey2_Ege_2024\27\27_B_9794 (1).txt')])
s = 20138
i = 0
j = len(l) - 1
ct = 0
right = 0
cmb = 0
while i < j:
    if l[i] + l[j] >= s:
        j -= 1
    elif l[i] + l[j] < s:
        i += 1
        ct += (len(l) - j) - 1
cmb = (len(l) - j - 1) * (len(l) - j) // 2
print(ct + cmb)