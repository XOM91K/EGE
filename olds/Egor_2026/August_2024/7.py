ct = int(input())
for i in range(ct):
    s = input()
    if len(s) == 6:
        g = 0
        if s[0] in 'ABCEHKMOPTXY':
            if s[1] in '1234567890':
                if s[2] in '1234567890':
                    if s[3] in '1234567890':
                        if s[4] in 'ABCEHKMOPTXY':
                            if s[5] in 'ABCEHKMOPTXY':
                                print('Yes')
                                g = 1
        if g == 0:
            print('No')