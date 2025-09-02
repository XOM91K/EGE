s = open(r'C:\Users\Zarif\Downloads\24_474.txt').readline()
s = s.replace('0', '#')
s = s.replace('2', '#')
s = s.replace('4', '#')
s = s.replace('6', '#')
s = s.replace('8', '#')
s = s.replace('1', '@')
s = s.replace('3', '@')
s = s.replace('5', '@')
s = s.replace('7', '@')
s = s.replace('9', '@')
for x in range(1, 1000):
    if '@' * x in s or '#' * x in s:
        print(x)