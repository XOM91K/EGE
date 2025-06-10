s = '>' + '3' * 10 + '5' * 10 + '7' * 10
while '>3' in s or '>5' in s or '>7' in s:
    if '>3' in s:
        s = s.replace('>3', '55>', 1)
    if '>5' in s:
        s = s.replace('>5', '5>3', 1)
    if '>7' in s:
        s = s.replace('>7', '3>5', 1)
s = s.replace('>', '')
print(sum(map(int, str(s))))