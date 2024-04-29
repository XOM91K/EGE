mx = []
for x in range(50):
    for y in range(50):
        for z in range(50):
            s = '0' + '1' * x + '2' * y + '3' * z + '0'
            while '00' not in s:
                s = s.replace('01', '120', 1)
                s = s.replace('02', '32013', 1)
                s = s.replace('03', '2210', 1)
            if s.count('1') == 27 and s.count('2') == 51:
                mx.append(x + y + z + 2)
print(max(mx))