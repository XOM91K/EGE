l = [int(x) for x in open('2.txt')]
mn_ch = 10 ** 10
for x in l:
    if x % 2 == 0:
        mn_ch = min(mn_ch, x)
ct = 0
for x in range(len(l) - 1):
    if (l[x] % 2 == 0 and l[x + 1] % 2 != 0) or (l[x] % 2 != 0 and l[x + 1] % 2 == 0):
        if abs(l[x + 1] - l[x]) == 2 and (min(l[x], l[x + 1]) + 1) % mn_ch == 0:
            ct += 1
    #print(l[x], l[x + 1])
print(ct)

# print(l)
# print(mn_ch)