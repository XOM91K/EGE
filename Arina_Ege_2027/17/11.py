l = [int(x) for x in open("11.txt")]
mx = []
for i in range(len(l) - 2):
    k = 0
    if str(abs(l[i]))[0] == str(abs(l[i]))[-1]:
        k += 1
    if str(abs(l[i+1]))[0] == str(abs(l[i+1]))[-1]:
        k += 1
    if str(abs(l[i+2]))[0] == str(abs(l[i+2]))[-1]:
        k += 1
    ck = 0
    if len(str(abs(l[i]))) == 5 and str(l[i])[-4] == '7':
        ck += 1
    if len(str(abs(l[i+1]))) == 5 and str(l[i + 1])[-4] == '7':
        ck += 1
    if len(str(abs(l[i+2]))) == 5 and str(l[i + 2])[-4] == '7':
        ck += 1
    if ck == 2 and k == 1:
        mx.append(max(l[i], l[i+1], l[i+2]))
print(len(mx), sum(mx))