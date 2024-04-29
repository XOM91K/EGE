s = '5' * 12 + '4' * 23 + '53' * 17
while '43' in s or '53' in s:
    if '43' in s:
        s = s.replace('43' ,'33', 1)
    else:
        s = s.replace('53', '433', 1)
print(s.count('3'))