s = open('42.txt').readline()
for d in range(26, 1, -1):
    for x in range(len(s) - (d - 1)):
        if len(set(s[x: x + d])) == d:
            print(d)
            exit()