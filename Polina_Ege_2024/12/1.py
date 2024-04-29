s = '6' * 79
while '2222' in s or '666' in s:
    if '2222' in s:
        s = s.replace('2222', '6', 1)
    else:
        s = s.replace('666', '2', 1)
print(s)