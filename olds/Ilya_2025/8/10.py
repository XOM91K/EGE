import itertools
c=0
for s in set(itertools.permutations('ТИМАШЕВСК')):
    s = ''.join(s)
    s = s.replace('И', 'А')
    s = s.replace('Е', 'А')
    s = s.replace('Т', 'В')
    s = s.replace('М', 'В')
    s = s.replace('Ш', 'В')
    s = s.replace('С', 'В')
    s = s.replace('К', 'В')
    if s[0] == 'В' and s[-1] =='В':
        if 'ВААВ' in s:
            c+=1
print(c)