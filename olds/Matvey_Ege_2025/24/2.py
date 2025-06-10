s = open(r'C:\Users\Zarif\Desktop\146_1 (6).txt').readline()
l = []
for i in range(10 ** 6 + 1):
    if sum(map(int, str(i))) ** len(str(i)) == i:
        l.append(i)
for i in l:
    if str(i) in s:
        print(i, s.count(str(i)))