#364
mn = []
for x in range(300):
    for y in range(300):
        s = '0' + '1' * x + '2' * y
        if x + y + 1 >= 95:
            while '01' in s or '02' in s:
                s = s.replace('02', '1110', 1)
                s = s.replace('01', '2210', 1)
            if str(sum(map(int, s))) == str(sum(map(int, s)))[::-1]:
                mn.append(x + y * 2)
print(min(mn))

# s = 'шалаш'
# print(str(s) == str(s)[::-1])
# s = '1822124712401232874632849751'
# print(s.count('1') * 1 + s.count('2') * 2 + s.count('8') * 8 + s.count('3') * 3 + s.count('4') * 4 + s.count('5') * 5 + s.count('6') * 6 + s.count('7') * 7 + s.count('9') * 9)
# print(sum(map(int, s))) #sumapints