for n in range(1, 100):
    s = '>' + '0' * 12 + '1' * n + '2' * 8
    while '>1' in s or '>2' in s or '>0' in s:
        if '>1' in s:
            s = s.replace('>1', '22>', 1)
        if '>2' in s:
            s = s.replace('>2', '2>', 1)
        if '>0' in s:
            s = s.replace('>0', '1>', 1)
    if (s.count('1') + s.count('2') * 2) == 68:
        print(n)

# print(d.count('1') + d.count('2') * 2 + d.count('3') * 3 + d.count('4') * 4 + d.count('5') * 5 + d.count('6') * 6 + d.count('7') * 7 + d.count('8') * 8 + d.count('9') * 9)
# print(sum(map(int, d)))