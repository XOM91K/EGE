l = [int(x) for x in open('2.txt')]
l = sorted(l)[::-1]
ct = 0
print(l)
i = 0
j = 1
while j != len(l):
    if l[i] - l[j] >= 8:
        ct += 1
        print(l[j])
        i = j
    j += 1
print(ct + 1)
# [43, 40, 3 9,38, 37,  32, 30]