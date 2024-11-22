s = '1' * 81
while '111' in s or '88' in s:
    if '88'in s:
        s = s.replace( '88', '1111')
    else:
        s = s.replace( '111', '8')
print(s)