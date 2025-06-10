s = open(r'C:\Users\Zarif\Downloads\146_1 (3).txt').readline()
r = []
for x in range(1, 10 ** 6 + 1):
    if sum(map(int, str(x))) ** len(str(x)) == x:
        r.append(x)
r = sorted(r)[::-1]
for x in r:
    print(s.count(str(x)), x)
#print(r)
#12300