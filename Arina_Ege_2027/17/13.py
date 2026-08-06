l = [int(x) for x in open("13.txt")]
mx = []
for i in range(len(l) - 2):
    k = 0
    if str(l[i])[0] == str(l[i])[-1]:
        k += 1
    if str(l[i + 1])[0] == str(l[i + 1])[-1]:
        k += 1
    if str(l[i + 2])[0] == str(l[i + 2])[-1]:
        k += 1
    if k == 1:
        ct = 0
        if str(l[i])[-3:-2] == "2" and len(str(abs(l[i]))) == 4:
            ct += 1
        if str(l[i + 1])[-3:-2] == "2" and len(str(abs(l[i + 1]))) == 4:
            ct += 1
        if str(l[i + 2])[-3:-2] == "2" and len(str(abs(l[i + 2]))) == 4:
            ct += 1
        if ct == 2:
            mx.append(max(l[i], l[i + 1], l[i + 2]))
print(len(mx), sum(mx))
