s = open(r'C:\Users\Zarif\Downloads\174_1 (10).txt').readline()
for x in range(26, 2, -1):
    for y in range(len(s) - 25):
        if len(set(s[y: x + y])) == x:
            print(x)
            exit()