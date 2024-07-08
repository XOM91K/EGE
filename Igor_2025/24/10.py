s = open('10.txt').readline()
ct = 3
mx = 0
for i in range(len(s) - 3):
    st = set(s[i] + s[i + 1] + s[i + 2] + s[i + 3])
    g = s[i] + s[i + 1] + s[i + 2] + s[i + 3]
    if not(len(st) == 1 and (st == {'Z'} or st == {'X'} or st == {'Y'})):
        if (g.count('X') == 2 and g.count('Y') == 2) or (g.count('X') == 2 and g.count('Z') == 2) or (g.count('Y') == 2 and g.count('Z') == 2):
            print(st)
            print(s[i] + s[i + 1] + s[i + 2] + s[i + 3])
            print(ct)
            ct += 1
            mx = max(mx, ct)
    else:
        ct = 3
print(mx)