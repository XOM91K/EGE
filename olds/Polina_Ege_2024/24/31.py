s = open(r'C:\Users\Zarif\Downloads\24_8_1709311597.txt').readline()
s = s.replace('ABA', '*')
s = s.replace('BAB', '*')
for x in range(0, 1000):
    if '*' * x in s:
        print(x)
