import string
s = open(r'C:\Users\Zarif\Downloads\24-277.txt').readline()
alf = '02468BCDFGHJKLMNPQRSTVWXZ'
for x in alf:
    s = s.replace(x, '.')
s = s.split('.')
mx = 0
for x in s:
    if len(x) > 2 and x[0].isdigit() and x[0] == x[-1]:
        if '1' not in x[1:-1] and '3' not in x[1:-1] and '5' not in x[1:-1] and '7' not in x[1:-1] and '9' not in x[1:-1]:
            print(x)
            mx = max(mx, len(x))
print(mx)