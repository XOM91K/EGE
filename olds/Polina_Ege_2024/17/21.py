l = [int(x) for x in open('21.txt')]
mx401 = 0
ct = 0
mn = 10 ** 100
for x in l:
    if x % 401 == 0:
        mx401 = max(mx401, x)
for x in range(len(l) - 2):
    if len(set([sum(map(int, str(l[x]))), sum(map(int, str(l[x + 1]))),sum(map(int, str(l[x + 2])))])) == 3:
        if l[x] + l[x + 1] + l[x + 2] > mx401:
            ct += 1
            mn = min(mn, l[x] + l[x + 1] + l[x + 2])
print(ct, mn)