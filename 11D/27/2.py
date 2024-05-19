#3231 kompege, кольцевая дорога
l = [int(x) for x in open('2.txt')]
ln = len(l)
rt_sm = [0] * ln
lf_sm = [0] * ln
for i in range(0, 1):
    for j in range(ln):
        if abs(j - i) < ln // 2 + 1:
            rt_sm[i] += l[j] * abs(j - i)
        else:
            lf_sm[i] += l[j] * (ln - abs(j - i))
l = l * 3
pr_l = [0] * (len(l) + 1)
for x in range(len(l)):
    pr_l[x + 1] = pr_l[x] + l[x]
for i in range(ln + 1, ln * 2):
    rt_sm[i - ln] = rt_sm[i - ln - 1] - l[i] - (pr_l[i + ln // 2] - pr_l[i + 1]) + l[i + ln // 2] * ln // 2
    lf_sm[i - ln] = lf_sm[i - ln - 1] - l[i - ln // 2] * (ln // 2 - 1) + (pr_l[i] - pr_l[i - ln // 2 + 1])
mn_sm = 10 ** 100
for x in range(len(rt_sm)):
    mn_sm = min(mn_sm, rt_sm[x] + lf_sm[x])
num = 0
for x in range(len(rt_sm)):
    if rt_sm[x] + lf_sm[x] == mn_sm:
        num = x + 1
print(num)