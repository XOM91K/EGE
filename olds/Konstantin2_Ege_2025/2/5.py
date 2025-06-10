print('a b c d')
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                if ((a <= b) and (not(b == c)) and (d <= a)) == 1:
                    print(a, b, c, d)