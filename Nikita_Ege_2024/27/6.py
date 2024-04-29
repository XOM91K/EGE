k = 137
l = [int(x) for x in open('6.txt')]
pf = [0] * (len(l) + 1)
for x in range(len(l)):
    pf[x + 1] = pf[x] + l[x]
mx_sm = 0
mx_ln = 0
for i in range(len(pf) - 1):
    for j in range(i + 1, len(pf)):
        if (pf[j] - pf[i]) % k == 0:
            if (pf[j] - pf[i]) >= mx_sm:
                mx_sm = (pf[j] - pf[i])
                mx_ln = abs(j - i)
print(mx_ln)