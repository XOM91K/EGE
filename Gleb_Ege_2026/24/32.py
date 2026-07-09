s = open(r'C:\Users\Zarif\Downloads\174_1 (15).txt').readline()
ct = 1
mx_ct = []
for k in range(26, 1, -1):
    for x in range(len(s) - k - 1):
        if len(set(s[x: x + k])) == k:
            print(k)