s = '9' * 100
while '33333' in s or '999' in s:
    if '33333' in s:
        s = s.replace('33333', '99', 1)
    else:
        s = s.replace('999', '3', 1)
print(s)
# s = '2222'
# s = s.replace('22', '%', 1)
# print(s)