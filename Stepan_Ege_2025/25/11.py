for x in range(206, 10 ** 8, 206):
    s = str(x)
    if s[-2:] == '56' and s[0:3] == '123':
        s = s.replace('0', 'Ч')
        s = s.replace('2', 'Ч')
        s = s.replace('4', 'Ч')
        s = s.replace('6', 'Ч')
        s = s.replace('8', 'Ч')
        s = s.replace('1', 'Н')
        s = s.replace('3', 'Н')
        s = s.replace('5', 'Н')
        s = s.replace('7', 'Н')
        s = s.replace('9', 'Н')
        if s[:3] == 'НЧН' and s[-4:] == 'НЧНЧ':
            print(x, x // 206)