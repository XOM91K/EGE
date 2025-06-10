import math
pr = []
for x in range(11):
    for y in range(11):
        for z in range(11):
            if x + y + z == 10:
                s = '0' * x + '4' * y + '1' * z + '<'
                while '4<' in s or '11<' in s or '00<' in s:
                    if '11<' in s:
                        s = s.replace('11<', '<9', 1)
                    if '4<' in s:
                        s = s.replace('4<', '<5', 1)
                    if '00<' in s:
                        s = s.replace('00<', '<92', 1)
                s = s.replace('<', '1')
                pr.append(math.prod(map(int, s)))
print(max(pr))