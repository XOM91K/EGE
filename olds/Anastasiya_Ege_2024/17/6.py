l = [int(x) for x in open('6.txt')]
summ = 10 ** 10
k = 0

l_151 = []
for i in range(len(l)):
    if abs(l[i]) % 1000 == 151:
        l_151.append(l[i])
l_151 = sum(l_151) / len(l_151)

for x in range(len(l) - 2):
    l_4 = []
    l_4.append(str(len(str(abs(l[x])))))
    l_4.append(str(len(str(abs(l[x + 1])))))
    l_4.append(str(len(str(abs(l[x + 2])))))
    if 1 <= l_4.count('4') < 3:
        last = []
        if l[x] % 13 == 0:
            last.append('1')
        elif l[x] % 7 == 0:
            last.append('0')
        if l[x + 1] % 13 == 0:
            last.append('1')
        elif l[x + 1] % 7 == 0:
            last.append('0')
        if l[x + 2] % 13 == 0:
            last.append('1')
        elif l[x + 2] % 7 == 0:
            last.append('0')
        # last.append(str(l[x + 1] % 100))
        # last.append(str(l[x + 2] % 100))
        if last.count('1') > last.count('0'):
            if l[x] > l_151 and l[x + 1] > l_151 and l[x + 2] > l_151:
                k += 1
                if l[x] + l[x + 1] + l[x + 2] < summ:
                    summ = l[x] + l[x + 1] + l[x + 2]

print(k, summ)