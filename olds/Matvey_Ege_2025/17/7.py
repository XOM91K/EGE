l = [int(x) for x in open('7.txt')]

ct1 = 0
sr = [x for x in l if str(x)[-2:] == '28']
sr = sum(sr) / len(sr)
ct2 = 0
mn_sum = 10**10
for i in range(len(l) - 2):
    ct1 = 0
    if len(str(abs(l[i]))) == 4 or len(str(abs(l[i + 1]))) == 4 or len(str(abs(l[i + 2]))) == 4:
        if str(l[i])[-2:] == '11':
            ct1 += 1
        if str(l[i + 1])[-2:] == '11':
            ct1 += 1
        if str(l[i + 2])[-2:] == '11':
            ct1 += 1
        if ct1 == 2:
            if l[i] > sr and l[i + 1] > sr and l[i + 2] > sr:
                ct2 += 1
                mn_sum = min(mn_sum, l[i] + l[i + 1] + l[i + 2])
print(ct2, mn_sum)