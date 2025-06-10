l = [int(x) for x in open('8.txt')]
mn21 = min([y for y in l if y > 0 and len(str(abs(y))) == 4 and sum(map(int, str(abs(y)))) == 21])
mx = []
for x in range(len(l) - 2):
    k = 0
    if len(str(abs(l[x]))) ==4 and sum(map(int, str(abs(l[x])))) == 15:
        k += 1
    if len(str(abs(l[x + 1]))) == 4 and sum(map(int, str(abs(l[x + 1])))) == 15:
        k += 1
    if len(str(abs(l[x + 2]))) == 4 and sum(map(int, str(abs(l[x + 2])))) == 15:
        k += 1
    if k == 2:
        if 98 * (l[x] + l[x + 1] + l[x + 2]) >= mn21 ** 2:
            mx.append(l[x] + l[x + 1] + l[x + 2])
print(len(mx), max(mx))