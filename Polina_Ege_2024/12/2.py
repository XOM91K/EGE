s = '5' + '6' * 152 + '5'
while '63' in s or '664' in s or '6665' in s:
    if '63' in s:
        s = s.replace('63', '4', 1)
    elif '664' in s:
        s = s.replace('664', '65', 1)
    elif '6665' in s:
        s = s.replace('6665', '663', 1)
print(s)