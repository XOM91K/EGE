print('a b c d')
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                if (a and (not b) or (a or b) and c or d) == 0:
                    print(a, b, c, d)