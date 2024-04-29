l = [int(x) for x in open('14.txt')]
ind_last = len(l) - 1
mx = 0
for x in range(len(l)):
    if abs(x - ind_last) >= 200:
        mx = max(mx, l[x])
print(mx + l[ind_last])