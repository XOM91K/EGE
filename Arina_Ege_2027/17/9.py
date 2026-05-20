l = [int(x) for x in open("9.txt")]
mn = len([x for x in l if abs(x) % 10 == 3 and len(str(abs(x))) == 4]) ** 2
mx = []
k = 0
for i in range(len(l) - 2):
    x = sorted([l[i], l[i+1], l[i+2]])
    if (x[1] + x[2]) > mn:
        mx.append(sum(x))
print(len(mx), max(mx))