l = [int(x) for x in open("15.txt")]
mx = []
mn = min([x for x in l if x > 0 and len(str(x)) == 4 and (int(str(x)[0]) + int(str(x)[1]) + int(str(x)[2]) + int(str(x)[3])) == 21])
for i in range(len(l) - 2):
    k = 0
    if len(str(abs(l[i]))) == 4 and (
            int(str(abs(l[i]))[0]) + int(str(abs(l[i]))[1]) + int(str(abs(l[i]))[2]) + int(str(abs(l[i]))[3])) == 15:
        k += 1
    if len(str(abs(l[i + 1]))) == 4 and (
            int(str(abs(l[i + 1]))[0]) + int(str(abs(l[i + 1]))[1]) + int(str(abs(l[i + 1]))[2]) + int(str(abs(l[i + 1]))[3])) == 15:
        k += 1
    if len(str(abs(l[i + 2]))) == 4 and (
            int(str(abs(l[i + 2]))[0]) + int(str(abs(l[i + 2]))[1]) + int(str(abs(l[i + 2]))[2]) + int(str(abs(l[i + 2]))[3])) == 15:
        k += 1
    if k == 2:
        if ((l[i] + l[i + 1] + l[i + 2]) * 98) >= mn ** 2:
            mx.append(l[i] + l[i + 1] + l[i + 2])
print(len(mx), max(mx))
