l = [int(x) for x in open('2_1.txt')]
M = 10
print(l)
#kk = 122
kk = 2
ct = 0
for i in range(len(l) - 2):
    for j in range(i + 1, len(l) - 1):
        for k in range(j + 1, len(l)):
            if j - i >= kk and k - j >= kk:
                if l[i] * l[j] * l[k] % M == 0:
                    print(l[i], l[j], l[k])
                    ct += 1
print(ct)