s = open(r'C:\Users\Zarif\Downloads\24_679.txt').readline()
s = s.replace('()', '#')
ct = 0
i = 0
for x in s:
    i += 1
    if x == '#':
        i += 1
        ct += 1
        if ct == 10000:
            print(i)
