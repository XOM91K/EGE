s = open(r'C:\Users\Zarif\Downloads\174_1 (6).txt').readline()
mx = []
for x in range(len(s) - 26):
    s2 = s[x]
    for y in range(1, 26):
        s2 += s[x + y]
        if len(set(s2)) == len(s2):
            mx.append(len(s2))
print(max(mx))
#SDFGHJKL