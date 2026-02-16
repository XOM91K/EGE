l = [int(x) for x in open('6.TXT')]
print(l)
l = sorted(l)
S = 7100
S2 = S
last_element = 0
while S - l[0] >= 0:
    S -= l[0]
    last_element = l[0]
    del l[0]
S += last_element
l.insert(0, last_element)
print(l)
ct = 0
for x in sorted(l, key=lambda d: -d):
    if S - x >= 0:
        S -= x
        break
    else:
        ct += 1
print(S2 - S, ct)