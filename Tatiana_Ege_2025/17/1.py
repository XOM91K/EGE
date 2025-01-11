l = [int(x) for x in open('1.txt')]
# l = open(r'C:\Users\Zarif\Downloads\153_1.txt')
# print('asdas\nasd')
#print(l)
sr = sum(l) / len(l)
ct = 0
mn = []
for x in range(len(l) - 1):
    if l[x] < sr or l[x + 1] < sr:
        if (l[x] % 7 == 0 and l[x] % 3 != 0 and l[x] % 11 != 0 and l[x] % 13 != 0) or (l[x + 1] % 7 == 0 and l[x + 1] % 3 != 0 and l[x + 1] % 11 != 0 and l[x + 1] % 13 != 0):
            ct += 1
            mn.append(l[x] + l[x + 1])
print(ct, min(mn))