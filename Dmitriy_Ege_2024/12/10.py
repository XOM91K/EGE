mn = []
for x in range(0, 100):
    for y in range(0, 100):
        if x + y >= 64:
            s = '0' + '1' * x + '2' * y
            while '01' in s or '02' in s:
                s = s.replace('02', '110', 1)
                s = s.replace('01', '2120', 1)
            sm = sum([int(d) for d in s])
            print(s, sm)
            if sm in [2, 4, 8, 16, 32, 64, 128, 256, 512 ,1024 ,2048]:
                mn.append(x + 2 * y)
            exit()
print(min(mn))