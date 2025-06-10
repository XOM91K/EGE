l = [int(x) for x in open('4.txt')]
s = [v for v in l if str(v)[-3:] == '151']
ss = sum(s) / len(s)
mx = []
for i in range(len(l) - 2):
    p = [z for z in [l[i],l[i+1],l[i+2]] if 999 < abs(z) < 10000]
    c = [d for d in [l[i],l[i+1],l[i+2]] if d % 13 == 0]
    cv = [b for b in [l[i],l[i+1],l[i+2]] if b % 7 == 0]
    if 1 <= len(p) <= 2:
        if len(c) > len(cv):
            if l[i] > ss and l[i+1] > ss and l[i+2] > ss:
                mx.append(l[i]+l[i+1]+l[i+2])
print(len(mx),min(mx))