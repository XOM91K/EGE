s = open('15.txt').readline()
l = []
for x in range(10**6 + 1):
    d = sum(map(lambda g: int(g) ** len(str(x)), str(x)))
    if d == x:
        l.append(d)
print(l)