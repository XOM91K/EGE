for n in range(4, 100):
    s = '2' + '5' * n
    while '25' in s or '35' in s or '555' in s:
        if '25' in s:
            s = s.replace('25', '53', 1)
        if '35' in s:
            s = s.replace('35', '2', 1)
        if '555' in s:
            s = s.replace('555', '23', 1)
    if sum(map(int, s)) % 7 == 0:
        print(n)
# s = '14219612091861409846213094862349824623940641092' # 7
# print(sum(map(int, s)))