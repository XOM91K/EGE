s = open('/Users/zarif/Downloads/174_1.txt').readline()
for x in range(26, 1, -1):
    for y in range(len(s) - x):
        if len(set(s[y: y + x])) == x:
            print(x)
            exit()