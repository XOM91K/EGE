l = [int(x) for x in open(r'C:\Users\Zarif\PycharmProjects\EGE\Sergey_Ege_2025\17\17-3.txt')]
ct = 0
mn = 10 ** 10
for x in range(len(l) - 1):
    if (l[x] * l[x + 1]) % 2 != 0 and ((l[x] + l[x + 1]) / 2) % 7 == 0:
        mn = min(mn, ((l[x] + l[x + 1]) / 2))
        ct += 1
print(ct, mn)