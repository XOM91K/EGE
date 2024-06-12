def return_symbols(s1, s2):
    s = ''
    if len(s1) < len(s2):
        for x in s1:
            if x in s2:
                s += x
    else:
        for x in s2:
            if x in s1:
                s += x
    return list(set(s))


s1 = 'Экскаватор'
s2 = 'Метеорит'
print(return_symbols(s1, s2))

