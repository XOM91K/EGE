s = open(r'C:\Users\Zarif\Downloads\24 (22).txt').readline()
for x in '0123456789':
    s = s.replace(x, '1')
if '111111111111' in s:
    print('ok')
print(len('111111111111'))