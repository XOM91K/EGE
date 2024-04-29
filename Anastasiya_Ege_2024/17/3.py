l = [int(x) for x in open('3.txt')]
m = 99999
ct = 0
for i in range(len(l) - 5):
    if l[i] + l[i+1] < l[i+2] + l[i+3] > l[i+4] + l[i+5]:
        if l[i] + l[i+1] > 0 and l[i+2] + l[i+3] > 0 and l[i+4] + l[i+5] > 0:
            ct += 1
            if m > l[i+2] * l[i+3]:
                m = l[i+2] * l[i+3]
print(ct, m)