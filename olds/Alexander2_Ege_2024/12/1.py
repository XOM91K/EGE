a = '8' * 45
while '1111' in a or '8888' in a:
    if '1111' in a:
        a = a.replace('1111', '88', 1)
    else:
        a = a.replace('8888', '11', 1)
print(a)