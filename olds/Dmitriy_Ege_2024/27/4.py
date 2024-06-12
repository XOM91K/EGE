l = [int(x) for x in open('4.txt')]
k = 324
l_sm = []
mx_sm = 0
for x in range(len(l) - 1):
    l_sm.clear()
    l_sm.append(l[x])
    for y in range(x + 1, len(l)):
        l_sm.append(l[y])
        if abs(x - y) >= k:
            mx_sm = max(mx_sm, sum(l_sm))
print(mx_sm)