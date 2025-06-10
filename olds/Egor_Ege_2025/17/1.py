l = [int(x) for x in open(r'C:\Users\Zarif\PycharmProjects\EGE\Egor_Ege_2025\17\1.txt')]
#print('asdsda\nasddsada')
sr = sum(l) / len(l)
ct = 0
mn = 10 ** 10
for x in range(len(l) - 1):
    if l[x] < sr or l[x + 1] < sr:
        if (l[x] % 7 == 0 and l[x] % 3 != 0 and l[x] % 11 != 0 and l[x] % 13 != 0) or (l[x + 1] % 7 == 0 and l[x + 1] % 3 != 0 and l[x + 1] % 11 != 0 and l[x + 1] % 13 != 0):
            ct += 1
            mn = min(mn, l[x] + l[x + 1])
print(ct, mn)