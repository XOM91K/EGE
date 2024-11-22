c = '9' *100
while '33333' in c or '999' in c:
    if '33333' in c:
        c=c.replace('33333','99', 1)
    else:
        c = c.replace('999','3',1)
print(c)