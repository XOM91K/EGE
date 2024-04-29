l = [int(x) for x in open('5.txt')]
l_28 = []
c = 0
minn = 10 ** 10

for i in range(len(l)):
    if abs(l[i]) % 100 == 28:
        l_28.append(l[i])
l_28 = sum(l_28) / len(l_28)
print(l_28)

for x in range(len(l) - 2):
    if len(str(abs(l[x]))) == 4 or len(str(abs(l[x + 1]))) == 4 or len(str(abs(l[x + 2]))) == 4:
        if ((abs(l[x]) % 100 == 11) and (abs(l[x + 1]) % 100 == 11) and (abs(l[x + 2]) % 100 != 11)) or ((abs(l[x]) % 100 != 11) and (abs(l[x + 1]) % 100 == 11) and (abs(l[x + 2]) % 100 == 11)) or ((abs(l[x]) % 100 == 11) and (abs(l[x + 1]) % 100 != 11) and (abs(l[x + 2]) % 100 == 11)):
            if l[x] > l_28 and l[x + 1] > l_28 and l[x + 2] > l_28:
                c += 1
                if l[x] + l[x + 1] + l[x + 2] < minn:
                    minn = l[x] + l[x + 1] + l[x + 2]
print(c, minn)