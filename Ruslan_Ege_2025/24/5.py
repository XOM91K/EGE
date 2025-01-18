s = open(r'C:\Users\Zarif\Downloads\146_1 (5).txt').readline()
ch = []
for x in range(10 ** 6 + 1):
    if sum(map(int, str(x))) ** len(str(x)) == x:
        ch.append(x)
print(ch)
for x in ch:
    print(s.count(str(x)), x)