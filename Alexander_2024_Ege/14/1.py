s = '0123456789abcdef'
for p in s:
    if p not in '0123456':
        for x in s[:s.index(p)]:
            for y in s[:s.index(p)]:
                for z in s[:s.index(p)]:
                    if (int(y + '3' + y, s.index(p)) + int(y + '65', s.index(p))) == int(x + '2' + z + '0', s.index(p)):
                        print(int(x+y+z, s.index(p)))