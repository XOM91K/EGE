l = [int(x) for x in open('20.txt')]
mx7 = max(d for d in l if str(abs(d))[-1] == '7')
mx = []
for x in range(len(l) - 1):
    if str(abs(l[x]))[0] == str(abs(l[x + 1]))[0]:
        k = 0
        if len(str(abs(l[x]))) == 3 and str(abs(l[x]))[-1] == '7':
            k += 1
        if len(str(abs(l[x + 1]))) == 3 and str(abs(l[x + 1]))[-1] == '7':
            k += 1
        if k >= 1:
            if (l[x] + l[x + 1]) < mx7:
                mx.append((l[x] + l[x + 1]))
print(len(mx), max(mx))