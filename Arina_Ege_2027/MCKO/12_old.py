s = '2' * 22 + '7' * 77
while '727' in s or '777' in s or '222' in s:
    if '222' in s:
        s = s.replace('222', '7', 1)
    else:
        if '777' in s:
            s = s.replace('777', '7', 1)
        else:
            s = s.replace('727', '2', 1)
print(s)