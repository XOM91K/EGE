l = [int(x) for x in open(r'C:\Users\Zarif\Downloads\27-99b.txt')]
ln = len(l)
l_s = 0
r_s = 0
mn_sm = 10 ** 1000
for j in range(ln):
    if abs(j) <= ln // 2:
        r_s += abs(j) * l[j]
    else:
        l_s += (ln % abs(j)) * l[j]
l = l * 3
pr_l = [0] * (len(l) + 1)
for x in range(len(l)):
    pr_l[x + 1] = pr_l[x] + l[x]
pkt = 0
for x in range(ln + 1, ln * 2):
    r_s = r_s - l[x] + (l[x + (ln // 2)] * (ln // 2)) - (pr_l[x + ln // 2] - pr_l[x + 1])
    l_s = l_s - (l[x - ln // 2] * (ln // 2 - 1)) + (pr_l[x] - pr_l[x - (ln // 2 - 1)])
    if r_s + l_s < mn_sm:
        mn_sm = r_s + l_s
        pkt = x - ln + 1
print(pkt)