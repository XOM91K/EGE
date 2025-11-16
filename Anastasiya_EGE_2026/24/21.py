s = open(r'C:\Users\Zarif\Downloads\174_1 (9).txt').readline()
for x in range(26, 1, -1):
    for y in range(0, len(s) - x):
        if len(set(s[y:y+x])) == x:
            print(x)
            exit()