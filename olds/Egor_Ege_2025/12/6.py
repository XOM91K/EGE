s = '>' + '12' * 30 + '13' * 10 + '41' * 10
while '>12' in s or '>13' in s or '>41' in s or '>31' in s:
    s = s.replace('>12', '32>')
    s = s.replace('>31', '21>')
    s = s.replace('>13', '41>')
    s = s.replace('>41', '23>')
print(s)
print(sum(map(int, s[:-1])))