a = [int(i) for i in open("4.txt")]
kr = []
ok = []
count = 0
p = []
d = []
for i in a:
    if i % 3 == 0:
        kr.append(i)
    if str(i)[-1] == '3':
        ok.append(i)
mini = min(kr)
maxi = max(ok)
for i in range(len(a) - 1):
    # 1
    # 2    3
    k = 0
    if mini <= a[i] <= maxi:
        k += 1
    if mini <= a[i + 1] <= maxi:
        k += 1
    if k == 1:
        count += 1
        p.append(a[i] ** 2 + a[i + 1] ** 2)
        d.append([a[i], a[i + 1]])
print(count)
print(min(p))