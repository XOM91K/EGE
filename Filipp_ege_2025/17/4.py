l = [int(x) for x in open('4.txt')]
mx = [x for x in l if str(x)[-1] == '7']
mx = max(mx)
ans = []
ct = 0
for x in range(len(l) - 2):
    l_4 = [abs(y) % 2 for y in [l[x], l[x + 1], l[x + 2]]]
    l_4 = [abs(y) % 2 for y in [l[x], l[x + 1], l[x + 2]]]
    if l_4.count(1) == 2:
        k = 0
        if l[x] > mx:
            k += 1
        if l[x + 1] > mx:
            k += 1
        if l[x + 2] > mx:
            k += 1
        if k == 1:
            ct += 1
            ans.append(l[x])
            ans.append(l[x + 1])
            ans.append(l[x + 2])
ans = set(ans)
sr = sum(ans) / len(ans)
print(ct, sr)
# print(ans)