l = sorted([[int(y) for y in x.split()] for x in open('13.txt')])
tm = [0] * 230
print(tm)
ct = 0
for x in l:
    for i in range(len(tm)):
        if x[0] > tm[i]:
            tm[i] = x[1]
            ct += 1
            print(i + 1)
            break

print(ct)