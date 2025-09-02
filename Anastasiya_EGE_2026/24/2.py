s = open(r'C:\Users\Zarif\Downloads\24_66 (1).txt').readline()
for x in range(1, 1000):
    if 'KOT' * x in s:
        print('Да есть', x, 'KOT' * x)
