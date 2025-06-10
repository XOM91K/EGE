for x in '012345789ABCDEFGHI':
    c1 = int(f'A3{x}74', 19)
    c2 = int(f'{x}40846', 19)
    if (c1 + c2) % 9 == 0:
        print((c1 + c2) // 9)