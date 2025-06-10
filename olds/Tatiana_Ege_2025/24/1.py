s = open(r'C:\Users\Zarif\Downloads\146_1 (7).txt').readline()
l = []
for x in range(1, 10 ** 6 + 1):
    if sum(map(int, str(x))) ** len(str(x)) == x:
        l.append(x)
l = sorted(l)[::-1]
for x in l:
    print(s.count(str(x)), x)
#20 9