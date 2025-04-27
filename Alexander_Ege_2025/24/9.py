s = [x.strip() for x in open(r'C:\Users\Zarif\Downloads\176_1 (3).txt')]
sp = []
for x in s:
    x = x.split('.')
    if x[0] == '195' and x[1][0] == '2' and x[-1] == '14':
        if 1 <= len(x[1]) <= 3:
            sp.append('.'.join(x))
print(len(set(s)))