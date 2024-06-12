l = [int(x) for x in open('20.txt')]
ct = 0
sl = [0] * 999
for x in range(len(l)):
    sl[l[x] % 999] += 1
    ct += sl[l[x] % 999]

print(ct)
