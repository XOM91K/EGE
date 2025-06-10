import string
alf = string.ascii_uppercase
i = 0
for x in alf:
    for y in alf:
        for z in alf:
            for w in alf:
                for q in alf:
                    for a in alf:
                        s = x + y + z + w + q + a
                        i += 1
                        if s == 'FEDABC':
                            print(i)
                            exit()
