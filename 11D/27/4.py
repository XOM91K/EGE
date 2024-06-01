#https://kompege.ru/variant?kim=25028282
l = [int(x) for x in open(r'C:\Users\Zarif\PycharmProjects\EGE\11D\27\27_B_9794 (1).txt')][2:]
l = sorted(l)
print(l)
i = 0
j = len(l) - 1
ct_pair = 0
while i < j:
    if l[i] + l[j] >= 20138:
        j -= 1
    else:
        i += 1
        ct_pair += (len(l) - j - 1)
print(ct_pair + (len(l) - j) * (len(l) - j - 1) // 2)