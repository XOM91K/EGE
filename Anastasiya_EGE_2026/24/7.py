s = open(r'C:\Users\Zarif\Downloads\24_439.txt').readline()
ct = 1
ct2 = 0
for x in range(len(s) - 1):
    if int(s[x]) < int(s[x + 1]):
        ct += 1
    else:
        if ct == 5:
            ct2 += 1
        ct = 1
print(ct2)