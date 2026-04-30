for x in '0123456789ABCDEFG':
    c1 = int(f'5432{x}67', 17)
    c2 = int(f'302{x}', 17)
    if (c1 + c2) % 19 == 0:
        print((c1 + c2))