s = open(r'C:\Users\Zarif\Downloads\174_1 (14).txt').readline()
for x in range(26, 1, -1):
    for y in range(len(s) - x):
        if len(set(s[y: y + x])) == x:
            print(x)
            exit()
