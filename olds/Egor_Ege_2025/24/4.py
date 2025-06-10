s = open(r'C:\Users\Zarif\Downloads\174_1 (5).txt').readline()
for x in range(26, 0, -1):
    for y in range(len(s) - x - 1):
        if len(set(s[y: y + x])) == len(s[y: y + x]):
            print(x)
            if x == 23:
                print(s[y: y + x])
            exit()